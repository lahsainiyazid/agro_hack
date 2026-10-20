#include "standard_scaler.hpp"


double [3] scale(double [3]features){
  //I will compute these later on the ml notebook
  double [3]means={1.0,1.0,1.0}; //Mean of 1->3 variable;
  double [3]std={1.0,1.0,1.0}; //Std of 1->3 variable;
  for (size_t i=0;i<features.size();i++){
    features[i]=(features[i]-means[i])/(std[i]);
  }
}
