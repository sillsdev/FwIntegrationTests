#!/bin/bash
for D in `find /home/vagrant/FwIntegrationTests/general_tests/*.sikuli -type d`
do
        echo Running $D ...
        sikuli $D
done
