# <em>Thrilltopia</em> 😉
## Project description
We are developing a reservation system for an imaginary activity centre called “Thrilltopia” based in Lisbon, Portugal.
Our app will display all the activities available at Thrilltopia allowing customers to browse through them and make a reservation. Current weather and forecast will be available on the website. To make a reservation the customer will click  on  their  chosen  activity  and  then  will  be  asked  to  give  their  first  and  last name,  phone  number,  pick  a  date  and  time,  then  select  the  number  of  people wanting  to  book  the  activity.  All  of  the  customers  will  be  provided  equipment needed to perform chosen activity. 
## How to run

### Python packages
The app includes a number of standard python libraries that do not need installation. Those are imported in the files that use them. The packages that need installation are in requirements.txt file
To install the required packages, follow steps below:
1. Open your command prompt or terminal.
2. Navigate to the project's directory using the `cd` command. For example:
```bash
cd /path-to-your-project
```
3. Run the following command to install the packages listed in the requirements.txt file:
```bash
pip install -r backend/requirements.txt
```
This will install all the packages and their specified versions listed in the requirements.txt file, ensuring that you have the correct dependencies for the project.

### SQL database
In backend/thrilltopia/database we added files needed to add database to MySQL Workbench. You should run schema_init.sql file in your Workbench which will create the database and populate it with data.

### Config file
Once you have database on your SQL Workbench, you'll need to create a config.json file in backend/thrilltopia folder.
We have included config_example.json, you can copy the details from that file to config.json and update your details: user, password, database name (if different), and host (if different).
Once you do that the app will be able to connect to your database.

### Getting API key for accessing the weather data from Visual Crossing
To obtain an API key for accessing weather data from Visual Crossing, follow these steps:

1. **Visit the Visual Crossing Weather Website**: Go to the [Visual Crossing Weather website](https://www.visualcrossing.com/).
2. **Sign Up or Log In**: If you already have an account, log in; otherwise, sign up for a new account.
3. **Access API Services**: After logging in, navigate to the Account section.
4. **Copy API Key**: Look for the </>Key symbol under "Your details" and copy the API key.
5. **Enter the correct application folder**: Incorporate the obtained API key into this application by entering the following folders: backend/thrilltopia.
6. **Insert API Key**: In your config.json file, search for the "api_key" inside "forecast_api" and replace with the key where it says YOUR_API_KEY.

### How to run the app
1. Make sure you followed all the steps before.
2. Start by running backend/thrilltopia/model.py.
3. Open the frontend/src/index.html file in your browser in order to interact with our app from a customers perspective.
4. You can also additionally run backend/thrilltopia/main.py check the console app, where you can see how it's looking from the clients view.

## Repository rules
### Pull request and commits naming convention
##### Reference to Jira
All pull requests and commits should start with Jira issue id from project: [Jira project board](https://software-4-group-4.atlassian.net/jira/software/projects/HG/boards/2).
##### Commit messages
Each commit should represent a self-contained unit of work that makes sense on its own. Commit messages should be brief and meaningful. After stating Jira issue id messages should start with imperative verb that describes what the commit does, such as 'add', 'fix', 'update' or 'refactor'.
For example:
```commandline
HG-38 Add repository naming convention to readme.md.
```
##### Pull requests
Pull request names should follow the same naming convention as commit messages while also having in mind wider scope of changes. All pull requests have to be reviewed and approved in order to merge. New reviewable commits pushed to a matching branch dismiss pull request review approvals.

### Branch naming convention
In order to track progress easier with Jira, branches are protected with rule "{feature,bugfix,test}/HG-[0-9]*-*". That rule allows to create branches only following naming convention that starts with either 'feature', 'bugfix' or 'test', followed by forward slash, Jira issue id and branch name. All words should be separated by hyphens.

For example:
```commandline
feature/HG-39-example-branch-name
```
