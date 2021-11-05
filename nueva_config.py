from PyQt5 import QtWidgets

from add_form import Ui_MainWindow

import modulos


class add(QtWidgets.QMainWindow):

    def __init__(acciones):
        super(add, acciones).__init__()

        acciones.ui = Ui_MainWindow()

        acciones.ui.setupUi(acciones)

        acciones.ui.btn_listo.clicked.connect(acciones.valores_reg)

        acciones.ui.ck_aut.clicked.connect(acciones.enable_auth)

        acciones.ui.ck_proxy.clicked.connect(acciones.enable_proxy)

    def valores_reg(acciones):
        nombre = acciones.ui.tb_nombre.text()
        ip = acciones.ui.tb_ip.text()
        mascara = acciones.ui.tb_mascara.text()
        puerta = acciones.ui.tb_puerta.text()
        dns1 = acciones.ui.tb_dns1.text()
        dns2 = acciones.ui.tb_dns2.text()

        if acciones.ui.ck_proxy.isChecked() == True:
            ip_proxy = acciones.ui.tb_ip_proxy.text()
            port_proxy = acciones.ui.tb_port_proxy.text()
        else:
            ip_proxy = "No tiene"
            port_proxy = "No tiene"

        if acciones.ui.ck_aut.isChecked() == True:
            user = acciones.ui.tb_name_user.text()
            passrd = acciones.ui.tb_password.text()
        else:
            user = "No tiene"
            passrd = "No tiene"

        modulos.crear_registros(nombre, ip, mascara, puerta, dns1, dns2, ip_proxy, port_proxy, user, passrd)

    def enable_proxy(acciones):
        if acciones.ui.ck_proxy.isChecked():
            acciones.ui.lbl_proxy_address.setEnabled(True)
            acciones.ui.lbl_port_proxy.setEnabled(True)
            acciones.ui.tb_ip_proxy.setEnabled(True)
            acciones.ui.tb_port_proxy.setEnabled(True)
            acciones.ui.ck_aut.setEnabled(True)
        else:
            acciones.ui.lbl_proxy_address.setEnabled(False)
            acciones.ui.lbl_port_proxy.setEnabled(False)
            acciones.ui.tb_ip_proxy.setEnabled(False)
            acciones.ui.tb_port_proxy.setEnabled(False)
            acciones.ui.ck_aut.setEnabled(False)

            acciones.ui.lbl_user.setEnabled(False)
            acciones.ui.lbl_pass.setEnabled(False)
            acciones.ui.tb_name_user.setEnabled(False)
            acciones.ui.tb_password.setEnabled(False)

    def enable_auth(acciones):
        if acciones.ui.ck_aut.isChecked():
            acciones.ui.lbl_user.setEnabled(True)
            acciones.ui.lbl_pass.setEnabled(True)
            acciones.ui.tb_name_user.setEnabled(True)
            acciones.ui.tb_password.setEnabled(True)
        else:
            acciones.ui.lbl_user.setEnabled(False)
            acciones.ui.lbl_pass.setEnabled(False)
            acciones.ui.tb_name_user.setEnabled(False)
            acciones.ui.tb_password.setEnabled(False)


ventana = QtWidgets.QApplication([])

programa = add()
