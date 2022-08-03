# Bitcoin Price Tracker Project - README
*** 
![](https://bitcoin.org/img/icons/logotop.svg?1637078881)  

**Instructions on how to compile/execute program(s):**  
*`crypto_machine.py`, `nomics.py`, and `tcp_client.py` should all be in the same directory*  
*In addition, ensure that line 23 in `tcp_client.py` has your Azure(Cloud) VM IP Address*  
1. Set up RPI  
    a. Connect LCD Screen to I2C-3  
    b. Connect Button to D8  
    c. Connect GREEN LED to D4  
    d. Connect RED LED to D3  
    e. Connect to Buzzer to D2  
2. Once SSH'd or in RPI terminal head to main directory of project  
    a. run `sudo pip3 install pytz`  
3. CD to **project_files**
4. Run **crypto_machine.py** via python3, `python3 crypto_machine.py`
5. In order to retrieve latest price of Bitcoin press the button
6. After the 10th update, you will receive a link to a recent trend line in the terminal. (Should be 9 button clicks the first time)  

*Green light indicates a increase in price from the previous collected price*  
*Red light indicates a decrease in price from the previous collected price*  
*If both lights turn on it means the price has not changed in the given time period*  
*The buzzer only rings when a change has occurred*  


**External libraries that were used:**
* time
* sys
* requests
* datetime
* pytz
* base64
* matplotlib
* pickle
* socket

**API's used:**
* [Nomics Bitcoin API](https://p.nomics.com/cryptocurrency-bitcoin-api)
* [IMGUR](https://api.imgur.com/)
* [IMGBB API](https://api.imgbb.com)

**SERVER SIDE FILES**  
When setting up your Azure (or any other cloud service) VM ensure to have the follow installed:  
1. `sudo apt install python3-pip`
2. `pip3 install matplotlib`
3. `sudo apt-get install python3-matplotlib`
4. `sudo apt-get install python3-tk`
5. `sudo apt-get install python3-psutil`

*Ensure that the IMGUR.py, plot_data.py, and tcp_server.py files are in the root of your VM*  
**IMGBB.py is left as a back up in case the IMGUR API is down, change line 42 on plot_data.py to IMGBB.url_call() to switch services**  
