#!/bin/sh

# This is an API service interface for up, runnig and testing
# the API. 

# Colour Variables

# 0    black     COLOR_BLACK     0,0,0
# 1    red       COLOR_RED       1,0,0
# 2    green     COLOR_GREEN     0,1,0
# 3    yellow    COLOR_YELLOW    1,1,0
# 4    blue      COLOR_BLUE      0,0,1
# 5    magenta   COLOR_MAGENTA   1,0,1
# 6    cyan      COLOR_CYAN      0,1,1
# 7    white     COLOR_WHITE     1,1,1
# tput sgr0 RESET

black=`tput setaf 0`
red=`tput setaf 1`
green=`tput setaf 2`
yellow=`tput setaf 3`
reset=`tput sgr0`
cyan=`tput setaf 6`

print_header ()
{
    clear
    echo "#######################################################################"
    echo "#                           ${cyan}Weather api v1.0${reset}                          #"
    echo "#                                                                     #"
    echo "#                        ${cyan}Created by Matias Zulberti${reset}                   #"
    echo "#######################################################################\n"
}
print_docker_is_runnnig ()
{
    echo "\n${green}Docker is start runnig ...${reset}\n"
}
print_docker_finish()
{
    echo "\n${green}Docker finish${reset}\n"
}

print_header
echo "This is an admin interface for up, running and testing the API\n"
echo "Please select one option to continue:\n"
echo "${cyan}1)${reset} Create images, up and running the entire app (only the first time)"
echo "${cyan}2)${reset} Run the app"
echo "${cyan}3)${reset} Test your app (only for development reasons)"
echo "${cyan}4)${reset} Cleaning up the project"
echo "${cyan}5)${reset} exit"

read option

clear

case $option in

    1)
        print_header
        echo "This option will create the images, run and up the containers."
        echo "But before we are going to see if the containers are already created.\n"
        echo "                  -----------------------------------                  "
        docker container ls -a | grep --colour=always wheaterapi_python_1
        echo "                  -----------------------------------                  "
        echo "\n"
        echo "If${green} wheaterapi_python_1${reset} appears in this list you only have to"
        echo "run the app." 
        echo "If you want re-build the app or the app's name is not present in the list"
        echo "press ${cyan}[y]${reset}"
        echo "If the app's name appears in the list press ${cyan}[n] ${reset}and run app"
        
        read option
        
        if [ $option = "y" ]
        then
            print_docker_is_runnnig
            docker rmi -f wheaterapi_python
            docker container rm wheaterapi_redis_1 wheaterapi_python_1
            docker-compose build
            docker-compose up
        else
            clear
            echo "${cyan}1)${reset} Running the app"
            echo "${cyan}2)${reset} Testing the app (only for development reasons)"
            echo "${cyan}3)${reset} Cleaning up the project"
            echo "${cyan}4)${reset} exit"
            echo "\n"
            echo "Please select one option to continue:"
            read option
            case $option in
                1)
                    print_header
                    print_docker_is_runnnig
                    docker-compose up
                ;;
                2)
                    print_header
                    echo "Let check if the image already exist. Does test-weatherapp image"
                    echo "appears in the list?\n"
                    echo "            ---------------------------------                 "
                    docker images | grep --colour=always test-weatherapp
                    echo "            ---------------------------------               \n"
                    echo "Please press to continue ${cyan}[Y/n]${reset}"
                    read option
                    if [ $option = "y"]
                    then
                        print_header
                        print_docker_is_runnnig
                        docker container run -it --name testContainer test-weatherapp
                        docker container rm testContainer
                        print_docker_finish
                        echo "${yellow}[INFO]${reset} The container was remove"
                        sleep 5
                        clear
                    else
                        print_header
                        print_docker_is_runnnig
                        docker build -t test-weatherapp:latest --file tests/test.dockerfile .
                        docker container run -it --name testContainer test-weatherapp
                        docker container rm testContainer
                        print_docker_finish
                        echo "${yellow}[INFO]${reset} The container was remove"
                        sleep 5
                        clear
                    fi
                ;;
                3)
                    print_header
                    print_docker_is_runnnig
                    docker rmi -f test-weatherapp wheaterapi_python
                    docker container rm testContainer wheaterapi_redis_1 wheaterapi_python_1
                    print_docker_finish
                    sleep 5
                    clear
                ;;
                4)
                    clear
                ;;
            esac
        fi
    ;;
    2)
        print_header
        print_docker_is_runnnig
        docker-compose up
        print_docker_finish
    ;;
    3)
        print_header
        echo "Let check if the image already exist. Does test-weatherapp image"
        echo "appears in the list?\n"
        echo "            ---------------------------------                 "
        docker images | grep --colour=always test-weatherapp
        echo "            ---------------------------------               \n"
        echo "Please press to continue ${cyan}[Y/n]${reset}"
        read option
        if [ $option = "y" ]
        then
            print_header
            print_docker_is_runnnig
            docker container run -it --name testContainer test-weatherapp
            docker container rm testContainer
            print_docker_finish
            echo "${yellow}[INFO]${reset} The container was remove"
            sleep 5
            clear
        else
            print_header
            print_docker_is_runnnig
            docker build -t test-weatherapp:latest --file tests/test.dockerfile .
            docker container run -it --name testContainer test-weatherapp
            docker container rm testContainer
            print_docker_finish
            echo "${yellow}[INFO]${reset} The container was remove"
            sleep 5
            clear
        fi
    ;;
    4)
        print_header
        print_docker_is_runnnig
        docker rmi test-weatherapp wheaterapi_python
        docker container rm testContainer wheaterapi_redis_1 wheaterapi_python_1
        print_docker_finish
        sleep 5
        clear
    ;;
    5)
        # echo "##########################################"
        # echo "#   Weather api is powered by FastAPI    #"
        # echo "#                                        #"
        # echo "#   FINAL WORDS:                         #"
        # echo "#               'God save the Queen'     #"
        # echo "##########################################"
        clear
    ;;
esac
