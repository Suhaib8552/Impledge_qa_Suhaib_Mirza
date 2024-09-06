from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

User= "kloudship.qa.automation@mailinator.com"
Pass= "Password1"


driver.get("https://ecs-qa.kloudship.com")

driver.find_element(By.ID,"login-email").send_keys(User)
driver.find_element(By.ID,"login-password").send_keys(Pass)
driver.find_element(By.ID,"login-btn").click()



print("Logged in Successfully")

driver.get("https://ecs-qa.kloudship.com/home")

print("Navigated to Home page")
driver.get("https://ecs-qa.kloudship.com/dashboard/store/all/packageType")

print("Navigated to Packages page")

driver.find_element(By.XPATH,"/html[1]/body[1]").click()

print("Add button Clicked")

driver.get("https://ecs-qa.kloudship.com/dashboard/store/all/packageType?id=new&mm=cGFja2FnZVR5cGU%3D&mmid=new")

name_inp = "Suhaib Mirza"
length_inp = "1"
height_inp = "1"
width_inp_inp = "1"


driver.find_element(By.XPATH, "/html[1]/body[1]/app-root[1]/app-sidenav[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/perfect-scrollbar[1]/div[1]/div[1]/div[1]/app-dashboard[1]/div[1]/div[2]/app-package-type-manage[1]/perfect-scrollbar[1]/div[1]/div[1]/mat-card[1]/form[1]/div[1]/div[1]/section[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]").send_keys(name_inp)
driver.find_element(By.XPATH, "/html[1]/body[1]/app-root[1]/app-sidenav[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/perfect-scrollbar[1]/div[1]/div[1]/div[1]/app-dashboard[1]/div[1]/div[2]/app-package-type-manage[1]/perfect-scrollbar[1]/div[1]/div[1]/mat-card[1]/form[1]/div[1]/div[2]/section[1]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]").send_keys(length_inp)
driver.find_element(By.XPATH, "/html[1]/body[1]/app-root[1]/app-sidenav[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/perfect-scrollbar[1]/div[1]/div[1]/div[1]/app-dashboard[1]/div[1]/div[2]/app-package-type-manage[1]/perfect-scrollbar[1]/div[1]/div[1]/mat-card[1]/form[1]/div[1]/div[2]/section[2]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]").send_keys(height_inp)
driver.find_element(By.XPATH, "/html[1]/body[1]/app-root[1]/app-sidenav[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/perfect-scrollbar[1]/div[1]/div[1]/div[1]/app-dashboard[1]/div[1]/div[2]/app-package-type-manage[1]/perfect-scrollbar[1]/div[1]/div[1]/mat-card[1]/form[1]/div[1]/div[2]/section[3]/div[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]").send_keys(width_inp)

print("Entered package details")


driver.find_element(By.XPATH, "/html[1]/body[1]/app-root[1]/app-sidenav[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/perfect-scrollbar[1]/div[1]/div[1]/div[1]/app-dashboard[1]/div[1]/div[2]/app-package-type-manage[1]/mat-toolbar[1]/button[1]/span[1]/mat-icon[1]").click()


print("Package added successfully")

driver.find_element(By.CLASS_NAME,"mat-focus-indicator mat-menu-trigger mat-tooltip-trigger mat-icon-button mat-button-base").click()
driver.find_element(By.XPATH,"(//button[@class='mat-focus-indicator mat-menu-item ng-tns-c99-1'])[1]").click()
driver.get("https://auth-qa.kloudship.com:97/api/auth?productId=6463855ae2026c7f51ac993f&grantType=PKCE&redirectUri=https://ecs-qa.kloudship.com&state=98d9889f-f28d-4884-9089-81e59b59e288&codeChallenge=05080002c472840f7d7694fb8859d1a77458279fa8ca615f47deb7184a0ed176")

#Delete a package

driver.find_element(By.ID,"login-email").send_keys(User)
driver.find_element(By.ID,"login-password").send_keys(Pass)
driver.find_element(By.ID,"login-btn").click()



print("Logged in Successfully")

driver.get("https://ecs-qa.kloudship.com/home")

print("Navigated to Home page")
driver.get("https://ecs-qa.kloudship.com/dashboard/store/all/packageType")

print("Navigated to Packages page")

driver.find_element(By.CLASS_NAME,"delete ng-star-inserted").click()
driver.get("https://ecs-qa.kloudship.com/dashboard/store/all/packageType?id=66db78e2074fcf91e0df2508")
driver.find(By.ID,"mat-focus-indicator mat-raised-button mat-button-base mat-primary ng-star-inserted")



driver.quit()













