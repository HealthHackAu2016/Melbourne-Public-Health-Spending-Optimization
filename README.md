# Background

Undernutrition causes 45% of child deaths per year and leads to 159 million stunted children. Early investment in nutritional interventions can build human capital and boost shared prosperity. The United Nation’s Sustainable Development Goals (SDGs) specify a 40% reduction in the number of stunted children by 2030. The World Bank estimates that this target will not be met without nutrition-specific interventions.

# Methods

Optima Nutrition is a tool to inform policy decisions in child nutrition. It consists of an epidemiological model which is integrated with economic and financial analysis frameworks and a formal mathematical optimisation routine. The model is a partial cohort model written in Python which tracks the health of children from birth to age five. Cost and coverage information about nutritional interventions are used to predict health outcomes such as death and stunting. A unique feature of Optima Nutrition is the optimisation function that is used to calculate the optimal allocation of resources to different program areas to minimise adverse outcomes. Additionally, it has capability to optimise funds across geographical regions, as well as being used for scenario forecasting.

# Team Memebers

Name		  	| work
------------- | -------------
Ruth  | Back end
Matt  | Back end
Sally	| Front end
Frank	| PM

# Tech Stack

 Name | Tech
------------- | -------------
Front End | Html CSS Bootstrap  
Database | sqlite3
Back End code | Python
API | Python flask

# Usage

1.  Ensure you are running Python 2 (verified to work on Python 2.7) with 'flask' installed.

2.  Clone this repository and 'cd' into it:

        $ git clone https://github.com/HealthHackAu2016/Melbourne-Public-Health-Spending-Optimization
        $ cd Melbourne-Public-Health-Spending-Optimization/backend

3.  Put the CSV file with your data in it, in the 'backend' directory, and ensure it has a '.csv' extension.

    The code expects a CSV of the following form:

        fval,Prophylactic zinc supplementation,Vitamin A supplementation,Complementary feeding education,Public provision of complementary foods,Breastfeeding promotion,Balanced energy-protein supplementation,Multiple micronutrient supplementation
        16707419.72,1591551.598,1.23E-12,23102844.5,4.91E-12,100.9444001,0,37.65997984

4.  Generate a database from the CSV. The database will be called 'database.db' in the 'backend' directory:

        $ python import_data.py

5.  Start the backend API:

        $ python api.py
         * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
         * Restarting with stat
         * Debugger is active!
         * Debugger pin code: 123-456-789

6.  Browse to http://127.0.0.1:5000/static/index.html

7.  Now you should be ready to run queries on your data!
