from test_helper import *
import flex_helper
import check_change

folder = home_folder + "/FwIntegrationTests/general_tests/helpers/images_for_comparison/"
backups_folder = home_folder + "/FwIntegrationTests/projects/"

# Open Tagbanwa
flex_helper.openFwBackup("Tagbanwa, Calamian 2015-07-07 1037 for testing purposes.fwbackup", 120)
wait(30)
check_change.check_dictionary(folder + "Tagbanwa - dictionary.png")
check_change.check_word("dalik", folder + "Tagbanwa - dalik.png") # IXTERMINATE
check_change.check_word("bugnawan", folder + "Tagbanwa - bugnawan.png")
App.focus("Tagbanwa")
click("1436902218392.png")

# Open Kamasau
flex_helper.openFwBackup("Kamasau 2015-07-07 1036 for testing purposes.fwbackup", 120)
wait(30)
check_change.check_dictionary(folder + "Kamasau - dictionary.png")
check_change.check_word("chiraq", folder + "Kamasau - chiraq.png") # like the French president in like the 2000s
check_change.check_word("gre", folder + "Kamasau - gre.png")
App.focus("Kamasau")
click("1436902218392.png")


# Open Ayta Mag-Anchi
flex_helper.openFwBackup("Ayta Mag-Anchi2 2015-07-07 1035 for testing purposes.fwbackup", 120)
wait(30)
check_change.check_text("kulot2.ptx", folder + "Ayta - kulot2.ptx.png")
App.focus("Ayta")
click("1436902218392.png")