<div align="right">
  <a style="margin-right:100px" href="https://www.linkedin.com/in/matiaszulberti/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.instagram.com/zulbertimatias/?hl=en"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white"></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="mailto:matiaszulberti@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>
</div>  

# WeatherAPI v1.0

## **Technologies**

    - PYTHON
    - FASTAPI

<br></br>

## **Get Started**

To run this app I crated a service shell script that provide you all the tools
you need to: Run, Deploy and Test. You have to follow some easy steps:

#### **Clone the respository in your local machine**

#### **Allow to the service authorization to run**

Open your linux terminal. Once you are in the root of the project. Run linux the following command:

`chmod -wx service.sh`

#### **Run the service**

Now you have to run: `./service.sh`


<br></br>

## **Diagrams**

### Flow Diagrama

![alt Flow diagram](img/Flow_diagram.png)

<br></br>

## **Response and Request examples**

Request Weather endpoint

`/api/v1/weather/?city=[city]&token_id=[token_id]`

![alt Request Weather info](img/request_weather_data.png)

Response from Weather endpoint

![alt Response Weather info](img/response_example.png)

## **Basic Auth API**

This version of the app has not so robust authentication layer. To use this app you have to use
add in the request this api token. 

**API token:** 3b719353762f7ddfc080e13556d248e8d8af1a63590b6d17738e4f57ac18a5d1

<br></br>

## **Project specifications**
