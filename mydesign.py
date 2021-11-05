from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon


class Ui_NetWork(object):
    def setupUi(self, NetWork):
        NetWork.setObjectName("NetWork")
        NetWork.resize(637, 573)
        NetWork.setMinimumSize(QSize(637, 573))
        NetWork.setMaximumSize(QSize(637, 573))
        NetWork.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(NetWork)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 16))
        self.label.setObjectName("label")
        self.cb_adaptadores = QtWidgets.QComboBox(self.centralwidget)
        self.cb_adaptadores.setGeometry(QtCore.QRect(10, 30, 381, 22))
        self.cb_adaptadores.setObjectName("cb_adaptadores")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 381, 251))
        self.groupBox.setObjectName("groupBox")
        self.lbl_MAC = QtWidgets.QLabel(self.groupBox)
        self.lbl_MAC.setGeometry(QtCore.QRect(10, 40, 271, 16))
        self.lbl_MAC.setObjectName("lbl_MAC")
        self.lbl_estado = QtWidgets.QLabel(self.groupBox)
        self.lbl_estado.setGeometry(QtCore.QRect(10, 20, 281, 16))
        self.lbl_estado.setObjectName("lbl_estado")
        self.lbl_DHCP = QtWidgets.QLabel(self.groupBox)
        self.lbl_DHCP.setGeometry(QtCore.QRect(10, 70, 231, 16))
        self.lbl_DHCP.setObjectName("lbl_DHCP")
        self.lbl_IP = QtWidgets.QLabel(self.groupBox)
        self.lbl_IP.setGeometry(QtCore.QRect(10, 100, 231, 16))
        self.lbl_IP.setObjectName("lbl_IP")
        self.lbl_mascara = QtWidgets.QLabel(self.groupBox)
        self.lbl_mascara.setGeometry(QtCore.QRect(10, 130, 281, 16))
        self.lbl_mascara.setObjectName("lbl_mascara")
        self.lbl_puerta = QtWidgets.QLabel(self.groupBox)
        self.lbl_puerta.setGeometry(QtCore.QRect(10, 160, 331, 16))
        self.lbl_puerta.setObjectName("lbl_puerta")
        self.lbl_DNSpre = QtWidgets.QLabel(self.groupBox)
        self.lbl_DNSpre.setGeometry(QtCore.QRect(10, 190, 261, 16))
        self.lbl_DNSpre.setObjectName("lbl_DNSpre")
        self.lbl_DNSalt = QtWidgets.QLabel(self.groupBox)
        self.lbl_DNSalt.setGeometry(QtCore.QRect(10, 220, 281, 16))
        self.lbl_DNSalt.setObjectName("lbl_DNSalt")
        self.btn_info_proxy = QtWidgets.QPushButton(self.groupBox)
        self.btn_info_proxy.setGeometry(QtCore.QRect(310, 210, 61, 28))
        self.btn_info_proxy.setObjectName("btn_info_proxy")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 70, 211, 251))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btn_add = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_add.setGeometry(QtCore.QRect(10, 20, 181, 28))
        self.btn_add.setObjectName("btn_add")
        self.btn_set = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_set.setGeometry(QtCore.QRect(10, 60, 151, 28))
        self.btn_set.setObjectName("btn_set")
        self.btn_edit = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_edit.setGeometry(QtCore.QRect(10, 100, 151, 28))
        self.btn_edit.setObjectName("btn_edit")
        self.btn_delete = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_delete.setGeometry(QtCore.QRect(10, 140, 141, 28))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_disable = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_disable.setGeometry(QtCore.QRect(10, 180, 141, 28))
        self.btn_disable.setObjectName("btn_disable")
        self.btn_about = QtWidgets.QPushButton(self.centralwidget)
        self.btn_about.setGeometry(QtCore.QRect(540, 10, 81, 28))
        self.btn_about.setObjectName("btn_about")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 380, 611, 181))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lbl_IP_info = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_IP_info.setGeometry(QtCore.QRect(10, 30, 231, 16))
        self.lbl_IP_info.setObjectName("lbl_IP_info")
        self.lbl_mascara_info = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_mascara_info.setGeometry(QtCore.QRect(10, 60, 281, 16))
        self.lbl_mascara_info.setObjectName("lbl_mascara_info")
        self.lbl_puerta_info = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_puerta_info.setGeometry(QtCore.QRect(10, 90, 321, 16))
        self.lbl_puerta_info.setObjectName("lbl_puerta_info")
        self.lbl_DNSpre_info = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_DNSpre_info.setGeometry(QtCore.QRect(10, 120, 261, 16))
        self.lbl_DNSpre_info.setObjectName("lbl_DNSpre_info")
        self.lbl_DNSalt_info = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_DNSalt_info.setGeometry(QtCore.QRect(10, 150, 281, 16))
        self.lbl_DNSalt_info.setObjectName("lbl_DNSalt_info")
        self.lbl_user_info = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_user_info.setGeometry(QtCore.QRect(350, 90, 241, 16))
        self.lbl_user_info.setObjectName("lbl_user_info")
        self.lbl_IP_proxy_info = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_IP_proxy_info.setGeometry(QtCore.QRect(350, 30, 211, 16))
        self.lbl_IP_proxy_info.setObjectName("lbl_IP_proxy_info")
        self.lbl_port_info = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_port_info.setGeometry(QtCore.QRect(350, 60, 171, 16))
        self.lbl_port_info.setObjectName("lbl_port_info")
        self.lbl_pass_info = QtWidgets.QLabel(self.groupBox_3)
        self.lbl_pass_info.setGeometry(QtCore.QRect(350, 120, 191, 16))
        self.lbl_pass_info.setObjectName("lbl_pass_info")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 330, 271, 16))
        self.label_2.setObjectName("label_2")
        self.cb_list_config = QtWidgets.QComboBox(self.centralwidget)
        self.cb_list_config.setGeometry(QtCore.QRect(10, 350, 381, 22))
        self.cb_list_config.setObjectName("cb_list_config")
        self.link_fijar = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.link_fijar.setGeometry(QtCore.QRect(390, 20, 71, 31))
        self.link_fijar.setObjectName("link_fijar")
        font = QtGui.QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(8)
        font.setUnderline(True)
        self.link_fijar.setFont(font)
        NetWork.setCentralWidget(self.centralwidget)
        icon = QIcon()
        icon.addFile(u"Network 1.ico", QSize(), QIcon.Normal, QIcon.Off)
        NetWork.setWindowIcon(icon)
        self.retranslateUi(NetWork)
        QtCore.QMetaObject.connectSlotsByName(NetWork)

    def retranslateUi(self, NetWork):
        _translate = QtCore.QCoreApplication.translate
        NetWork.setWindowTitle(_translate("NetWork", "Net.Work"))
        self.label.setText(_translate("NetWork", "Seleccione el Adaptador de Red:"))
        self.groupBox.setTitle(_translate("NetWork", "Información del adaptador seleccionado"))
        self.lbl_MAC.setText(_translate("NetWork", "Dirección MAC:"))
        self.lbl_estado.setText(_translate("NetWork", "Estado de conexión:"))
        self.lbl_DHCP.setText(_translate("NetWork", "Estado DHCP:"))
        self.lbl_IP.setText(_translate("NetWork", "Dirección IP actual:"))
        self.lbl_mascara.setText(_translate("NetWork", "Máscara de sub red:"))
        self.lbl_puerta.setText(_translate("NetWork", "Puerta de enlace predeterminada:"))
        self.lbl_DNSpre.setText(_translate("NetWork", "DNS preferido:"))
        self.lbl_DNSalt.setText(_translate("NetWork", "DNS alternativo:"))
        self.groupBox_2.setTitle(_translate("NetWork", "Cuadro de acciones disponibles"))
        self.btn_add.setText(_translate("NetWork", "Añadir configuracion de red"))
        self.btn_set.setText(_translate("NetWork", "Establecer configuración"))
        self.btn_edit.setText(_translate("NetWork", "Modificar configuración"))
        self.btn_delete.setText(_translate("NetWork", "Eliminar configuración"))
        self.btn_disable.setText(_translate("NetWork", "Desabilitar adaptador"))
        self.btn_about.setText(_translate("NetWork", "Acerca de"))
        self.groupBox_3.setTitle(_translate("NetWork", "Información de la configuración seleccionada:"))
        self.lbl_IP_info.setText(_translate("NetWork", "Dirección IP actual:"))
        self.lbl_mascara_info.setText(_translate("NetWork", "Máscara de sub red:"))
        self.lbl_puerta_info.setText(_translate("NetWork", "Puerta de enlace predeterminada:"))
        self.lbl_DNSpre_info.setText(_translate("NetWork", "DNS preferido:"))
        self.lbl_DNSalt_info.setText(_translate("NetWork", "DNS alternativo:"))
        self.lbl_user_info.setText(_translate("NetWork", "Nombre de usuario:"))
        self.lbl_IP_proxy_info.setText(_translate("NetWork", "Dirección proxy:"))
        self.lbl_port_info.setText(_translate("NetWork", "Puerto del proxy:"))
        self.lbl_pass_info.setText(_translate("NetWork", "Contraseña:"))
        self.label_2.setText(_translate("NetWork", "Seleccione la configuración que desea aplicar:"))
        self.link_fijar.setText(_translate("NetWork", "Fijar"))
        self.btn_info_proxy.setText(_translate("NetWork", "Proxy"))
