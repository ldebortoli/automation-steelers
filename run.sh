#!/bin/bash

browsers="default";
headless="false";

# Get command line params
while getopts e:b:c:m:-: flag
do 
    case "${flag}" in
        -)
            case "${OPTARG}" in
                headless) headless="true";;
            esac;;

        b) browsers=${OPTARG};;
    esac
done

# Print params
echo -e "\n\n------ INPUTS ------\n";
echo "Browsers: ${browsers}";
echo "Headless: ${headless}";

# Get OS
OS="$(uname -s)";
if [[ "$OS" == "Darwin" ]]; then OS="MAC"; fi

# Run the automation code for specific browser
for browser in $browsers; do

    # Run the tests with the params
    echo -e "\n\n------ START TESGING ON ${OS} USGING ${browser} BROWSER ------\n\n" | tr a-z A-Z;
    pipenv run python3 -m pytest -n logical --html=reports/report-${browser}.html --self-contained-html --browser=${browser}
    echo -e "\n\n------ TESTING ON ${OS} USING ${browser} BROWSER FINISHED ------" | tr a-z A-Z;

done

echo -e "\n\nAll tests finished\n";


