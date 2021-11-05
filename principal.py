import psutil
from PyQt5 import QtWidgets
from mydesign import Ui_NetWork
from PyQt5.QtWidgets import QMessageBox
import sys
import modulos
from winreg import *
import winreg
import nueva_config

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):

        super(mywindow, self).__init__()

        self.ui = Ui_NetWork()

        self.ui.setupUi(self)

        self.ui.btn_delete.clicked.connect(self.for_delete)

        self.ui.btn_edit.clicked.connect(self.for_edit)

        self.ui.cb_list_config.currentTextChanged.connect(self.show_info)

        self.ui.cb_adaptadores.currentTextChanged.connect(self.show_info_adapter)

        self.ui.btn_add.clicked.connect(self.popWindow)

        self.ui.btn_set.clicked.connect(self.for_set_config)

        self.ui.btn_info_proxy.clicked.connect(self.get_proxy)

        self.ui.link_fijar.clicked.connect(self.to_pin_adapter)

        ##self.get_config()
        self.get_adapters()

    def get_adapters(self):
        inter = psutil.net_if_addrs().keys()
        for item in inter:
            self.ui.cb_adaptadores.addItem(item)
        try:
            lugar = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Net.Work\\")
            fijado = winreg.QueryValueEx(lugar, "fijado")
            self.ui.cb_adaptadores.setCurrentText(fijado[0])
        except OSError:
            pass

    def get_config(self):
        aKey = OpenKey(HKEY_CURRENT_USER, "SOFTWARE\\Net.Work", 0, KEY_ALL_ACCESS)
        try:
            i = 0
            while True:
                asubkey = EnumKey(aKey, i)
                self.ui.cb_list_config.addItem(asubkey)
                i += 1
        except WindowsError:
            pass

    def for_edit(self):
        msg = QMessageBox()
        selection = self.ui.cb_list_config.currentText()
        if selection == "":
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Debe seleccionaar alguna de las configuraciones existentes antes de realizar esta acción.")
            msg.setWindowTitle("Estado")
            msg.exec_()
        else:
            modulos.modificar_config(selection)

    def for_delete(self):
        msg = QMessageBox()
        selection = self.ui.cb_list_config.currentText()
        if selection == "":
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Debe seleccionaar alguna de las configuraciones existentes antes de realizar esta acción.")
            msg.setWindowTitle("Estado")
            msg.exec_()
        else:
            modulos.eliminar_config(selection)
            self.ui.cb_list_config.clear()
            self.get_config()

    def show_info(self):
        try:
            selection = self.ui.cb_list_config.currentText()
            lugar = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, f"SOFTWARE\\Net.Work\\{selection}", 0,
                                     winreg.KEY_ALL_ACCESS)

            ip = winreg.QueryValueEx(lugar, "ip")
            mascara = winreg.QueryValueEx(lugar, "mascara")
            puerta = winreg.QueryValueEx(lugar, "puerta")
            dns1 = winreg.QueryValueEx(lugar, "dns1")
            dns2 = winreg.QueryValueEx(lugar, "dns2")
            ip_proxy = winreg.QueryValueEx(lugar, "ip_proxy")
            port_proxy = winreg.QueryValueEx(lugar, "port_proxy")
            user_proxy = winreg.QueryValueEx(lugar, "user_proxy")
            pass_proxy = winreg.QueryValueEx(lugar, "pass_proxy")

            self.ui.lbl_IP_info.setText(f"Dirección IP: {ip[0]}")
            self.ui.lbl_mascara_info.setText(f"Máscara de subred: {mascara[0]}")
            self.ui.lbl_puerta_info.setText(f"Puerta de enlace predeterminada: {puerta[0]}")
            self.ui.lbl_DNSpre_info.setText(f"DNS preferido: {dns1[0]}")
            self.ui.lbl_DNSalt_info.setText(f"DNS alternativo: {dns2[0]}")
            self.ui.lbl_IP_proxy_info.setText(f"Dirección proxy: {ip_proxy[0]}")
            self.ui.lbl_port_info.setText(f"Puerto proxy: {port_proxy[0]}")
            self.ui.lbl_user_info.setText(f"Nombre de usuario: {user_proxy[0]}")
            self.ui.lbl_pass_info.setText(f"Contraseña: {pass_proxy[0]}")
        except OSError as e:
            pass

    def popWindow(self):
        nueva_config.programa.ui.tb_nombre.setText("")
        nueva_config.programa.ui.tb_ip.setText("")
        nueva_config.programa.ui.tb_mascara.setText("255.255.255.0")
        nueva_config.programa.ui.tb_puerta.setText("")
        nueva_config.programa.ui.tb_dns1.setText("")
        nueva_config.programa.ui.tb_dns2.setText("")
        nueva_config.programa.ui.tb_ip_proxy.setText("")
        nueva_config.programa.ui.tb_port_proxy.setText("")
        nueva_config.programa.ui.tb_name_user.setText("")
        nueva_config.programa.ui.tb_password.setText("")

        nueva_config.programa.show()

    def for_set_config(self):
        msg = QMessageBox()
        selection = self.ui.cb_list_config.currentText()
        adaptador = self.ui.cb_adaptadores.currentText()
        if selection == "":
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Debe seleccionaar alguna de las configuraciones existentes antes de realizar esta acción.")
            msg.setWindowTitle("Estado")
            msg.exec_()
        else:
            modulos.set_config(selection, adaptador)

    def show_info_adapter(self):
        try:
            nombre = self.ui.cb_adaptadores.currentText()
            get_mac = psutil.net_if_addrs().get(nombre)
            self.ui.lbl_MAC.setText(f"Dirección física(MAC): {get_mac[0][1]}")

            get_status = psutil.net_if_stats().get(nombre)
            if get_status[0] == True:
                self.ui.lbl_estado.setText("Estado de conexión: Conectado")
            else:
                self.ui.lbl_estado.setText("Estado de conexión: Desconectado")

            lugar = r"SYSTEM\CurrentControlSet\Control\Network\{4D36E972-E325-11CE-BFC1-08002BE10318}"
            reg_key = OpenKeyEx(HKEY_LOCAL_MACHINE,
                                r"SYSTEM\CurrentControlSet\Control\Network\{4D36E972-E325-11CE-BFC1-08002BE10318}")
            i = 0
            while True:
                try:
                    asubkey = EnumKey(reg_key, i)
                    i += 1
                    if asubkey == "Descriptions":
                        pass
                    else:
                        abierta = OpenKey(HKEY_LOCAL_MACHINE, f"{lugar}\\{asubkey}\\Connection")
                        file = QueryValueEx(abierta, "Name")
                        if file[0] == nombre:
                            reg_key = OpenKeyEx(HKEY_LOCAL_MACHINE, r"SYSTEM\ControlSet001\Services"
                                                                    r"\Tcpip\Parameters\Interfaces\\" + asubkey)
                            dhcp_status = QueryValueEx(reg_key, "EnableDHCP")
                            if dhcp_status[0] == 0:
                                self.ui.lbl_DHCP.setText(f"Estado DHCP: Deshabilitado")
                                ip = QueryValueEx(reg_key, "IPAddress")
                                mascara = QueryValueEx(reg_key, "SubnetMask")
                                try:
                                    puerta = QueryValueEx(reg_key, "DefaultGateway")
                                    for i in puerta[0]:
                                        prueba = i
                                    self.ui.lbl_puerta.setText(f"Puerta de enlace predeterminada: {prueba}")
                                except WindowsError:
                                    pass
                                try:
                                    dns = QueryValueEx(reg_key, "NameServer")
                                    dns1 = dns[0]
                                    for i in dns1:
                                        if i == ",":
                                            pos = dns1.index(i)
                                            dns_pre_show = dns1[:pos]
                                            dns_alt_show = dns1[pos + 1:]

                                            self.ui.lbl_DNSpre_info.setText(f"DNS preferido: {dns_pre_show}")
                                            self.ui.lbl_DNSalt_info.setText(f"DNS alternativo: {dns_alt_show}")
                                except WindowsError:
                                    pass

                                self.ui.lbl_IP.setText(f"Dirección IP actual: {ip[0]}")
                                self.ui.lbl_mascara.setText(f"Máscara de sub red: {mascara[0]}")
                                break
                            else:
                                self.ui.lbl_DHCP.setText(f"Estado DHCP: Habilitado")
                                ip = QueryValueEx(reg_key, "DhcpIPAddress")
                                mascara = QueryValueEx(reg_key, "DhcpSubnetMask")
                                try:
                                    puerta = QueryValueEx(reg_key, "DhcpDefaultGateway")
                                    for i in puerta[0]:
                                        puerta = i
                                    self.ui.lbl_puerta.setText(f"Puerta de enlace predeterminada: {puerta}")
                                except WindowsError:
                                    pass
                                try:
                                    dns = QueryValueEx(reg_key, "DhcpNameServer")
                                    dns1 = dns[0]
                                    for i in dns1:
                                        if i == ",":
                                            pos = dns1.index(i)
                                            dns_pre_show = dns1[:pos]
                                            dns_alt_show = dns1[pos + 1:]

                                            self.ui.lbl_DNSpre_info.setText(f"DNS preferido: {dns_pre_show}")
                                            self.ui.lbl_DNSalt_info.setText(f"DNS alternativo: {dns_alt_show}")
                                except WindowsError:
                                    pass

                                self.ui.lbl_IP.setText(f"Dirección IP actual: {ip[0]}")
                                self.ui.lbl_mascara.setText(f"Máscara de sub red: {mascara[0]}")
                                break
                except WindowsError:
                    self.ui.lbl_IP.setText("Dirección IP actual: No tiene")
                    self.ui.lbl_mascara.setText("Máscara de sub red: No tiene")
                    self.ui.lbl_puerta.setText("Puerta de enlace predeterminada: No tiene")
                    self.ui.lbl_DNSpre_info.setText("DNS preferido: No tiene")
                    self.ui.lbl_DNSalt_info.setText("DNS alternativo: No tiene")
                    break
        except:
            pass

    def get_proxy(self):
        global pass_proxy, user_proxy, port_proxy_show, ip_proxy_show
        msg = QMessageBox()
        lugar_proxy = OpenKeyEx(HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings")
        proxy_enable = QueryValueEx(lugar_proxy, "ProxyEnable")
        if proxy_enable[0] == 1:
            ip_proxy = QueryValueEx(lugar_proxy, "ProxyServer")
            server = ip_proxy[0]
            for i in server:
                if i == ":":
                    pos = server.index(i)
                    ip_proxy_show = server[:pos]
                    port_proxy_show = server[pos + 1:]
                    user_proxy = QueryValueEx(lugar_proxy, "ProxyUser")
                    pass_proxy = QueryValueEx(lugar_proxy, "ProxyPass")

            msg.setIcon(QMessageBox.Information)
            msg.setText(f"IP del servidor: {ip_proxy_show}\n"
                        f"Puerto del servidor: {port_proxy_show}\n\n"
                        f"Nombre de usuario: {user_proxy[0]}\n"
                        f"Contraseña: {pass_proxy[0]}")
            msg.setWindowTitle("Información del proxy")
            msg.exec_()
        else:
            msg.setIcon(QMessageBox.Critical)
            msg.windowIcon()
            msg.setText("La configuración del proxy esta desactivada.")
            msg.setWindowTitle("Información")
            msg.exec_()

    def to_pin_adapter(self):
        try:
            msg = QMessageBox()
            adaptador = self.ui.cb_adaptadores.currentText()
            lugar = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Net.Work\\")

            winreg.SetValueEx(lugar, "fijado", 0, winreg.REG_SZ, adaptador)

            msg.setIcon(QMessageBox.Information)
            msg.setText("El adaptador a sudo fijado exitosamente.")
            msg.setWindowTitle("Información")
            msg.exec_()
        except:
            pass


app = QtWidgets.QApplication([])

application = mywindow()

application.show()

sys.exit(app.exec())
