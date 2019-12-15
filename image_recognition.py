import os
import sys
import cv2
import numpy as np

# This is the template you are searching for
template_image = r'C:\dev\Python\python_opencv\images\template_ocean_city.jpg'

# This is the image you are searching
screenshot_image = r'C:\dev\Python\python_opencv\images\screenshot_maryland_map.jpg'

# Giving OpenCV a threshold around 97% works best
threshold = 0.97

class ImageSolution:

	def __init__(self, template_image, screenshot_image, threshold):
	
		self._template_image = template_image
		self._screenshot_image = screenshot_image
		self._threshold = threshold

		self._template_width = None
		self._template_height = None
		self._screen = None
		self._loc = None

		
	def calculate_template_match_coordinates(self):
	
		self._screen = cv2.imread(self._screenshot_image)
		gray_screen = cv2.cvtColor(self._screen, cv2.COLOR_BGR2GRAY)

		template = cv2.imread(template_image, 0)
		self._template_width, self._template_height = template.shape[::-1]
		
		# There are several algorithm options. This example shows 'TM_CCOEFF_NORMED'. Check out the OpenCV documentation for the others.
		result = cv2.matchTemplate(gray_screen, template, cv2.TM_CCOEFF_NORMED)

		# A threshold around 97% works best.
		self._loc = np.where(result >= self._threshold)


	def display_results(self):
		"""Display the results in a window with a red rectangle around the matches.
		"""
		print("\nScreenshot Path:")
		print("  " + str(screenshot_image))
		print("\nTemplate Path:")
		print("  " + str(template_image))
		print("\nTemplate Dimensions:")
		print("  width = " + str(self._template_width))
		print("  height = " + str(self._template_height))

		print("\n\n=== Matches ===")
		for pt in zip(*self._loc[::-1]):
			print("\n  Match found:")
			print("    Upper-left match coordinate = " + str(pt))
			print("    Lower-right match coordinate = " + str( (pt[0] + self._template_width, pt[1] + self._template_height) ))
			cv2.rectangle(self._screen, pt, (pt[0] + self._template_width, pt[1] + self._template_height), (0, 0, 255), 2)
		cv2.imshow("Python OpenCV - Template Matching Demo", self._screen)
		cv2.waitKey(0)
		cv2.destroyAllWindows()


if __name__ == '__main__':
	solution = ImageSolution(template_image, screenshot_image, threshold)
	solution.calculate_template_match_coordinates()
	solution.display_results()
	print('\n\nCOMPLETED... image_recognition.py :)\n')