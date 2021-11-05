import winreg
from PyQt5.QtWidgets import QMessageBox
import nueva_config



def crear_registros(nombre, ip, puerta, mascara, dns1, dns2, ip_proxy, port_proxy, user, password):
    msg = QMessageBox()

    try:
        lugar = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Net.Work\\" + nombre)

        winreg.SetValueEx(lugar, "config_name", 0, winreg.REG_SZ, nombre)

        winreg.SetValueEx(lugar, "ip", 0, winreg.REG_SZ, ip)

        winreg.SetValueEx(lugar, "mascara", 0, winreg.REG_SZ, mascara)

        winreg.SetValueEx(lugar, "puerta", 0, winreg.REG_SZ, puerta)

        winreg.SetValueEx(lugar, "dns1", 0, winreg.REG_SZ, dns1)

        winreg.SetValueEx(lugar, "dns2", 0, winreg.REG_SZ, dns2)

        winreg.SetValueEx(lugar, "ip_proxy", 0, winreg.REG_SZ, ip_proxy)

        winreg.SetValueEx(lugar, "port_proxy", 0, winreg.REG_SZ, port_proxy)

        winreg.SetValueEx(lugar, "user_proxy", 0, winreg.REG_SZ, user)

        winreg.SetValueEx(lugar, "pass_proxy", 0, winreg.REG_SZ, password)

        msg.setIcon(QMessageBox.Information)
        msg.setText("La configuración ha sido guardada exitosamente.")
        msg.setWindowTitle("Estado")
        msg.exec_()
    except OSError as e:
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ha ocurrido un error, por favor, revise los datos.")
        msg.setWindowTitle("Estado")
        msg.exec_()


def eliminar_config(nombre):
    msg = QMessageBox()
    try:
        lugar = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Net.Work\\", 0, winreg.KEY_ALL_ACCESS)

        winreg.DeleteKey(lugar, nombre)

        msg.setIcon(QMessageBox.Information)
        msg.setText("La configuración ha sido eliminada exitosamente.")
        msg.setWindowTitle("Estado")
        msg.exec_()
    except OSError as e:
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ha ocurrido un error, por favor, revise los datos.")
        msg.setWindowTitle("Estado")
        msg.exec_()


def modificar_config(nombre):
    try:
        lugar = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, f"SOFTWARE\\Net.Work\\{nombre}", 0,
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

        nueva_config.programa.ui.tb_nombre.setText(nombre)
        nueva_config.programa.ui.tb_ip.setText(ip[0])
        nueva_config.programa.ui.tb_mascara.setText(mascara[0])
        nueva_config.programa.ui.tb_puerta.setText(puerta[0])
        nueva_config.programa.ui.tb_dns1.setText(dns1[0])
        nueva_config.programa.ui.tb_dns2.setText(dns2[0])
        nueva_config.programa.ui.tb_ip_proxy.setText(ip_proxy[0])
        nueva_config.programa.ui.tb_port_proxy.setText(port_proxy[0])
        nueva_config.programa.ui.tb_name_user.setText(user_proxy[0])
        nueva_config.programa.ui.tb_password.setText(pass_proxy[0])

        if ip_proxy[0] == "No tiene":
            pass
        else:
            nueva_config.programa.ui.ck_proxy.setChecked(True)
            nueva_config.programa.ui.lbl_proxy_address.setEnabled(True)
            nueva_config.programa.ui.lbl_port_proxy.setEnabled(True)
            nueva_config.programa.ui.tb_ip_proxy.setEnabled(True)
            nueva_config.programa.ui.tb_port_proxy.setEnabled(True)
            nueva_config.programa.ui.ck_aut.setEnabled(True)

        if user_proxy[0] == "No tiene":
            pass
        else:
            nueva_config.programa.ui.ck_aut.setChecked(True)
            nueva_config.programa.ui.lbl_user.setEnabled(True)
            nueva_config.programa.ui.lbl_pass.setEnabled(True)
            nueva_config.programa.ui.tb_name_user.setEnabled(True)
            nueva_config.programa.ui.tb_password.setEnabled(True)

        nueva_config.programa.show()
    except OSError as e:
        print("mal")


def set_config(nombre, adaptador):
    try:
        msg = QMessageBox
        lugar = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Net.Work\\" + nombre)

        ip = winreg.QueryValueEx(lugar, "ip")
        mascara = winreg.QueryValueEx(lugar, "mascara")
        puerta = winreg.QueryValueEx(lugar, "puerta")
        dns1 = winreg.QueryValueEx(lugar, "dns1")
        dns2 = winreg.QueryValueEx(lugar, "dns2")
        ip_proxy = winreg.QueryValueEx(lugar, "ip_proxy")
        port_proxy = winreg.QueryValueEx(lugar, "port_proxy")
        user_proxy = winreg.QueryValueEx(lugar, "user_proxy")
        pass_proxy = winreg.QueryValueEx(lugar, "pass_proxy")

        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Estado")
        msg.setText(f"Estás seguro que desea aplicar la configuración: {nombre} en el adaptador {adaptador}?")
        resultado = msg.result()
        if resultado == msg.result(QMessageBox.Yes):
            print("")
        msg.exec_()
    except OSError as e:
        print("mal")