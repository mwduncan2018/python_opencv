import os
import sys
import cv2
import numpy as np

# Template Image = the template you are searching for
template_image = r''
# Screenshot Image = the image you are searching
screenshot_image = r''

class ImageSolution:

	def __init__(self, template_image, screenshot_image):
		print(template_image)
		print(screenshot_image)
		self._template_image = template_image
		self._screenshot_image = screenshot_image
		self._screen = None
		self._loc = None
		
	def calculate_template_match_coordinates(self):
		self._screen = cv2.imread(self._screenshot_image)
		gray_screen = cv2.cvtColor(self._screen, cv2.COLOR_BGR2GRAY)
		template = cv2.imread(template_image, 0)
		w, h = template.shape[::-1]
		print("Template shape:")
		print("w = " + str(w))
		print("h = " + str(h))
		print("")
		result = cv2.matchTemplate(gray_screen, template, cv2.TM_CCOEFF_NORMED)
		print("result type is .... " + str(type(result)))
		print("")
		print("Result:")
		print(result)
		print("")
		threshold = 0.97
		self._loc = np.where(result >= threshold)
		print("")
		print("loc:")
		print(self._loc)
		
	def write_results_to_file(self, write_file):
		"""Writes the results to a file so Java can consume.
		"""
		f = open(write_file, 'w')
		num_matches = 0
		for pt in zip(*self._loc[::-1]):
			num_matches = num_matches + 1
			f.write(str(pt) + '\n')
			print("Match found...")
			print("   Upperleft  = " + str(pt))
			print("   Upperright = " + str( (pt[0] + w, pt[1] + h) ))
			cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
		if num_matches == 0:
			f.write('None')
		print("Number of Matches = " + str(num_matches))
		f.close()

	def display_results(self):
		"""Display the results in a window with a red rectangle around the matches.
		"""
		cv2.imshow("screen", self._screen)
		cv2.waitKey(0)
		cv2.destroyAllWindows()


if __name__ == '__main__':
	# Uncomment if running from the command line
	#template_image = sys.argv[1]
	#screenshot_image = sys.argv[2]
	#reult_path = sys.argv[3]

	sol = ImageSolution(template_image, screenshot_image)
	sol.calculate_template_match_coordinates()
	#sol.write_results_to_file(result_path)
	sol.display_results()

	print('COMPLETED... image_solution.py :)')
	#w, h = template.shape[::-1]
	#print(str(w))
	#print(str(h))