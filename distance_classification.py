import cv2

# Load the first image (Faculty Image)
faculty_img = cv2.imread("Plaksha_Faculty.jpg")
if faculty_img is None:
    print("Error: Could not load plaksha_Faculty.jpg")
else:
    cv2.imshow("Plaksha Faculty", faculty_img)

# Load the second image (Template Image)
template_img = cv2.imread("Dr_Shashi_Tharoor.jpg")
if template_img is None:
    print("Error: Could not load Dr_Shashi_Tharoor.jpg")
else:
    cv2.imshow("Dr Shashi Tharoor", template_img)
