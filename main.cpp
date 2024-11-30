#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include <stdlib.h>

#include <stdexcept>
#include <vector>
#include <iostream>
#include <string>

namespace py = pybind11;

/**
 * @brief Exception class to throw when object in the critical range is noticed 
 */
class ObjectTooCloseForComfort : public std::exception {
private:
	std::string msg;
public:
/**
 * @brief Constructor for ObjectTooCloseForComfort
 *
 * @param message Error message
 */
	ObjectTooCloseForComfort(std::string message) : msg(message) {
	}


/**
 * @brief Get error message
 * 
 * @return message as a c_string
 */
	const char* what() const noexcept override {
		return msg.c_str();
  }
};

/**
 * @brief Check if there are any objects closer that objectStreshold
 * 
 * Throws an ObjectTooCloseForComfort if there is a object closer than criticalStreshold
 *
 * @param numpyData         depthMap as numpy array
 * @param objectStreshold   Streshold for elements to notify
 * @param criticalStreshold Streshold for elements to notify
 * @param width             width of the depthMap
 * @param height            height of the depthMap
 *
 * @return list of objects closer than the objectStreshold
 */
std::vector<std::tuple<int,int,double>> addVec(py::array_t<double> numpyData, double objectStreshold, double criticalStreshold, int width, int height){
	double* cData = static_cast<double*>(numpyData.request().ptr);
	std::vector<std::tuple<int,int,double>>retVec;
	double closest = 10000;

	#pragma omp parallel
	{
		double closestLocal = 10000;
		std::vector<std::tuple<int,int,double>>localVec;

		#pragma omp for schedule(static,1)
		for (int ii = 0;ii < width*height;ii++){


			if (cData[ii] < closestLocal){
				closestLocal = cData[ii];
			}
			if (cData[ii] < objectStreshold){
				int xCoord = ii % width;
				int yCoord = ii / width;
				double dist = cData[ii];
				localVec.push_back(std::tuple<int,int,double>(xCoord, yCoord, dist));
			}
		}
		#pragma omp critical
		{
			retVec.insert(
					retVec.end(), 
					localVec.begin(), 
					localVec.end()
			);
			if (closestLocal < closest){
				closest = closestLocal;
			}
		}
	}
	if (closest < criticalStreshold){
		throw ObjectTooCloseForComfort(std::string("Object too close for comfort. Distance is ")+std::to_string(closest));
	}

	return retVec;
}

PYBIND11_MODULE(example, m) {
	m.def("addVec", &addVec, "A function that adds two vectors");

	// py::register_exception<ObjectTooCloseForComfort>(m, "ObjectTooCloseForComfort");
	py::register_exception<ObjectTooCloseForComfort>(m, "ObjectTooCloseForComfort", PyExc_Exception);
}
