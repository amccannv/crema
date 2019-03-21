# ENV_LIB = env/lib/python3.6
# ENV_CV2 = $(ENV_LIB)/cv2.so

# # Find cv2 library for the global Python installation.
# GLOBAL_CV2 := $(shell /usr/bin/python -c 'import cv2; print(cv2)' | awk '{print $$4}' | sed s:"['>]":"":g)

# # Link global cv2 library file inside the virtual environment.
# $(ENV_CV2): $(GLOBAL_CV2) env
# 	cp $(GLOBAL_CV2) $@

# env: requirements.txt
# 	test -d env || virtualenv env
# 	. env/bin/activate && pip install -r requirements.txt

# test: $(ENV_CV2)
# 	. env/bin/activate && python -c 'import cv2; print(cv2)'

# clean:
# 	rm -rf env