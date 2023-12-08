
    /*
    This inline function was automatically generated using DecisionTreeToCpp Converter

    It takes feature vector as single argument:
    feature_vector[0] - cost
feature_vector[1] - cunumberpel
feature_vector[2] - currbtdepth
feature_vector[3] - currdepth
feature_vector[4] - currmtdepth
feature_vector[5] - currqtdepth
feature_vector[6] - currtrdepth
feature_vector[7] - diagavg
feature_vector[8] - diagsad
feature_vector[9] - diavar
feature_vector[10] - diffminmax
feature_vector[11] - distortion
feature_vector[12] - fracbits
feature_vector[13] - height
feature_vector[14] - max
feature_vector[15] - min
feature_vector[16] - modetype
feature_vector[17] - qp
feature_vector[18] - pelavg
feature_vector[19] - pelcornersavg
feature_vector[20] - peldiffdiagonal
feature_vector[21] - peldifffullcorneravg
feature_vector[22] - squaredcu
feature_vector[23] - videoresheight
feature_vector[24] - videoreswidth
feature_vector[25] - treetype
feature_vector[26] - width
feature_vector[27] - prevpocheight
feature_vector[28] - prevpocwidth
feature_vector[29] - thisheightminusprevheight
feature_vector[30] - thiswidthminusprevwidth
feature_vector[31] - thissizeminusprevsize
feature_vector[32] - target


    It returns index of predicted class:
    0 - 0
1 - 1


    Simply include this file to your project and use it
    */

    #include <vector>

inline int decidir_particionamento(const std::vector<double> & feature_vector) 
{
	if (feature_vector.at(31) <= 256.0) {
		if (feature_vector.at(28) <= 48.0) {
			if (feature_vector.at(10) <= 90.5) {
				if (feature_vector.at(0) <= 27313275.0) {
					if (feature_vector.at(11) <= 12245.0) {
						if (feature_vector.at(10) <= 67.5) {
							return 0;
						}
						else {
							return 1;
						}
					}
					else {
						if (feature_vector.at(12) <= 1066013.0) {
							return 0;
						}
						else {
							return 0;
						}
					}
				}
				else {
					if (feature_vector.at(10) <= 70.5) {
						if (feature_vector.at(21) <= 597.5) {
							return 1;
						}
						else {
							return 0;
						}
					}
					else {
						if (feature_vector.at(0) <= 29497399.0) {
							return 0;
						}
						else {
							return 1;
						}
					}
				}
			}
			else {
				if (feature_vector.at(17) <= 24.5) {
					if (feature_vector.at(15) <= 352.5) {
						if (feature_vector.at(11) <= 10873.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
					else {
						if (feature_vector.at(10) <= 147.5) {
							return 0;
						}
						else {
							return 1;
						}
					}
				}
				else {
					if (feature_vector.at(10) <= 163.5) {
						if (feature_vector.at(12) <= 1556264.0) {
							return 0;
						}
						else {
							return 0;
						}
					}
					else {
						if (feature_vector.at(12) <= 1508497.0) {
							return 0;
						}
						else {
							return 1;
						}
					}
				}
			}
		}
		else {
			if (feature_vector.at(10) <= 90.5) {
				if (feature_vector.at(12) <= 1319841.5) {
					if (feature_vector.at(17) <= 24.5) {
						if (feature_vector.at(10) <= 61.5) {
							return 0;
						}
						else {
							return 0;
						}
					}
					else {
						if (feature_vector.at(10) <= 61.5) {
							return 0;
						}
						else {
							return 0;
						}
					}
				}
				else {
					if (feature_vector.at(12) <= 2184040.5) {
						if (feature_vector.at(19) <= 511.5) {
							return 0;
						}
						else {
							return 0;
						}
					}
					else {
						if (feature_vector.at(0) <= 4395015.25) {
							return 1;
						}
						else {
							return 0;
						}
					}
				}
			}
			else {
				if (feature_vector.at(30) <= -16.0) {
					if (feature_vector.at(10) <= 118.5) {
						if (feature_vector.at(12) <= 1065558.5) {
							return 0;
						}
						else {
							return 0;
						}
					}
					else {
						if (feature_vector.at(12) <= 9157048.0) {
							return 0;
						}
						else {
							return 0;
						}
					}
				}
				else {
					if (feature_vector.at(10) <= 166.5) {
						if (feature_vector.at(17) <= 29.5) {
							return 0;
						}
						else {
							return 0;
						}
					}
					else {
						if (feature_vector.at(11) <= 6104140.5) {
							return 0;
						}
						else {
							return 0;
						}
					}
				}
			}
		}
	}
	else {
		if (feature_vector.at(10) <= 200.5) {
			if (feature_vector.at(31) <= 640.0) {
				if (feature_vector.at(10) <= 83.5) {
					if (feature_vector.at(10) <= 41.5) {
						if (feature_vector.at(19) <= 42.0) {
							return 0;
						}
						else {
							return 0;
						}
					}
					else {
						if (feature_vector.at(12) <= 1618945.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
				}
				else {
					if (feature_vector.at(17) <= 29.5) {
						if (feature_vector.at(17) <= 24.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
					else {
						if (feature_vector.at(10) <= 142.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
				}
			}
			else {
				if (feature_vector.at(10) <= 85.5) {
					if (feature_vector.at(23) <= 1620.0) {
						if (feature_vector.at(17) <= 24.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
					else {
						if (feature_vector.at(10) <= 71.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
				}
				else {
					if (feature_vector.at(17) <= 29.5) {
						if (feature_vector.at(10) <= 121.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
					else {
						if (feature_vector.at(10) <= 141.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
				}
			}
		}
		else {
			if (feature_vector.at(31) <= 832.0) {
				if (feature_vector.at(31) <= 640.0) {
					if (feature_vector.at(10) <= 301.5) {
						if (feature_vector.at(17) <= 34.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
					else {
						if (feature_vector.at(10) <= 556.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
				}
				else {
					if (feature_vector.at(10) <= 583.5) {
						if (feature_vector.at(10) <= 309.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
					else {
						if (feature_vector.at(10) <= 813.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
				}
			}
			else {
				if (feature_vector.at(10) <= 585.5) {
					if (feature_vector.at(23) <= 1620.0) {
						if (feature_vector.at(10) <= 368.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
					else {
						if (feature_vector.at(0) <= 4517039.25) {
							return 1;
						}
						else {
							return 1;
						}
					}
				}
				else {
					if (feature_vector.at(24) <= 2880.0) {
						if (feature_vector.at(17) <= 29.5) {
							return 1;
						}
						else {
							return 1;
						}
					}
					else {
						if (feature_vector.at(0) <= 5429201.25) {
							return 1;
						}
						else {
							return 1;
						}
					}
				}
			}
		}
	}
}