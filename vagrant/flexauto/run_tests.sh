#!/bin/bash
export DISPLAY=:0.0

### Change screen resolution
xrandr --output VGA-0 --mode 1024x768

### Sikuli XScripts
runsikulix -r /home/vagrant/FwIntegrationTests/general_tests/_sikuli_runall.sikuli

exit
