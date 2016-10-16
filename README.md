# Background

Undernutrition causes 45% of child deaths per year and leads to 159 million stunted children. Early investment in nutritional interventions can build human capital and boost shared prosperity. The United Nation’s Sustainable Development Goals (SDGs) specify a 40% reduction in the number of stunted children by 2030. The World Bank estimates that this target will not be met without nutrition-specific interventions.

Optima Nutrition is a tool to inform policy decisions in child nutrition. It consists of an epidemiological model which is integrated with economic and financial analysis frameworks and a formal mathematical optimisation routine. The model is written in Python and tracks the health of children from birth to age five. Cost and coverage information about nutritional interventions are used to predict health outcomes such as death and stunting. A unique feature of Optima Nutrition is the optimisation function that is used to calculate the optimal allocation of resources to different program areas to minimise adverse outcomes.  The tool is used to make recommendations about which interventions a country should prioritise funding towards.

# Health Hack Challenge

Sometimes a country is not able to implement the spending recommendation due to political reasons or other funding constraints.  The challenge for Health Hack 2016 was to create a tool for policy makers to interact quickly and directly with the data.  Before the weekend, the interventions parameter space for an example country in Asia was sampled (this is computationly intensive).  The samples focused on the outcome of stunting by the year 2030 and were put into a csv file for use over the weekend.

# Health Hack Product

The team built a web-based user interface to explore the data.  On the left hand side the optimal recommended spending allocation is displayed with the number of cases of stunting by 2030 in this best case scenario.  The middle panel allows the policy makers to add their own contraints on any of the interventions via a 'max' and a 'min' value.  On clicking the 'Go' button the interface displays on the right hand side the best spending recommendation with these constraints, and the corresponding number of cases of stunting in this constrained scenario.

 

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

5.  Start the backend API (make sure you are in the backend directory still):

        $ python api.py
         * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
         * Restarting with stat
         * Debugger is active!
         * Debugger pin code: 123-456-789

6.  Browse to http://127.0.0.1:5000/static/index.html

7.  Now you should be ready to run queries on your data!
