from instagramLoginPage import InstagramLogIn
from instagramHomePage import InstagramHome
from selenium import webdriver

username = input("Kullanıcı Adınızı Giriniz.")
password = input("Kullanıcı Şifrenizi Giriniz.")

driver = webdriver.Chrome()

instaLog = InstagramLogIn(username , password , driver)
instaHome = InstagramHome(driver)

instaLog.signIn()

instaHome.getFollowers()

