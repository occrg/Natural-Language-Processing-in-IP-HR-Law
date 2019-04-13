clean-executable:
	rm -rf build
	rm -rf dist

build-executable:
	pyinstaller -F -c App-UI.py --hidden-import=statsmodels.tsa.statespace._kalman_filter --hidden-import=statsmodels.tsa.statespace._kalman_smoother --hidden-import=statsmodels.tsa.statespace._representation --hidden-import=statsmodels.tsa.statespace._simulation_smoother --hidden-import=statsmodels.tsa.statespace._statespace --hidden-import=statsmodels.tsa.statespace._tools --hidden-import=statsmodels.tsa.statespace._filters._conventional --hidden-import=statsmodels.tsa.statespace._filters._inversions --hidden-import=statsmodels.tsa.statespace._filters._univariate --hidden-import=statsmodels.tsa.statespace._smoothers._alternative --hidden-import=statsmodels.tsa.statespace._smoothers._classical --hidden-import=statsmodels.tsa.statespace._smoothers._conventional --hidden-import=statsmodels.tsa.statespace._smoothers._univariate
