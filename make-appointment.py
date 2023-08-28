import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class Appointment(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
		self.url = "https://katalon-demo-cura.herokuapp.com/"

	def st_login(self):
		driver = self.browser
		driver.get(self.url)
		driver.find_element(By.CLASS_NAME, "btn.btn-dark.btn-lg.toggle").click()

		driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
		driver.find_element(By.ID, "txt-username").send_keys("John Doe")
		driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
		driver.find_element(By.ID, "btn-login").click()

		respon = driver.find_element(By.CLASS_NAME, "col-sm-12.text-center").text
		self.assertIn('Make Appointment', respon)

		driver.quit()

	def test_make_appointment(self):
		driver = self.browser
		driver.get(self.url)
		driver.find_element(By.ID, "btn-make-appointment").click()

		respon = driver.find_element(By.CLASS_NAME, "lead").text
		self.assertIn('Please login to make appointment.', respon)

		#login first
		driver.find_element(By.ID, "txt-username").send_keys("John Doe")
		driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
		driver.find_element(By.ID, "btn-login").click()

		#make appointment
		respon = driver.find_element(By.CLASS_NAME, "col-sm-12.text-center").text
		self.assertIn('Make Appointment', respon)
		
		drop_facility = driver.find_element(By.ID, "combo_facility")
		select = Select(drop_facility)
		
		select.select_by_value("Seoul CURA Healthcare Center")
		
		driver.find_element(By.ID, "chk_hospotal_readmission").click()

		driver.find_element(By.ID, "radio_program_medicaid").click()

		driver.find_element(By.ID, "txt_visit_date").click()
		driver.find_element(By.XPATH, "/html/body/div/div[1]/table/tbody/tr[3]/td[4]").click()

		driver.find_element(By.ID, "btn-book-appointment").click()

		#check the appointment
		respon = driver.find_element(By.ID, "facility").text
		self.assertIn('Seoul CURA Healthcare Center', respon)

		respon = driver.find_element(By.ID, "visit_date").text
		self.assertIn('16/08/2023', respon)

		#history menu's
		driver.find_element(By.CLASS_NAME, "btn.btn-dark.btn-lg.toggle").click()
		driver.find_element(By.XPATH, "//a[normalize-space()='History']").click()

		respon = driver.find_element(By.CLASS_NAME, "col-sm-12.text-center").text
		self.assertIn('History', respon)
		
		#profile menu's
		driver.find_element(By.CLASS_NAME, "btn.btn-dark.btn-lg.toggle").click()
		driver.find_element(By.XPATH, "//a[normalize-space()='Profile']").click()

		respon = driver.find_element(By.CLASS_NAME, "lead").text
		self.assertIn('Under construction.', respon)

		driver.quit()

	def st_history(self):
		driver = self.browser
		driver.get(self.url)
		driver.find_element(By.CLASS_NAME, "btn.btn-dark.btn-lg.toggle").click()

		driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
		driver.find_element(By.ID, "txt-username").send_keys("John Doe")
		driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
		driver.find_element(By.ID, "btn-login").click()

		driver.find_element(By.XPATH, "//a[normalize-space()='History']").click()

		respon = driver.find_element(By.CLASS_NAME, "col-sm-12.text-center").text
		self.assertIn('History', respon)

	def st_profile(self):
		driver = self.browser
		driver.get(self.url)
		driver.find_element(By.CLASS_NAME, "btn.btn-dark.btn-lg.toggle").click()

		driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
		driver.find_element(By.ID, "txt-username").send_keys("John Doe")
		driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
		driver.find_element(By.ID, "btn-login").click()

		driver.find_element(By.XPATH, "//a[normalize-space()='Profile']").click()

		respon = driver.find_element(By.CLASS_NAME, "lead").text
		self.assertIn('Under construction.', respon)

if __name__ == "__main__":
	unittest.main()