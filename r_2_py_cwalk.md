# **R to Python Data Science Task Equivalents**

This table provides **Python equivalents** for common R data science tasks.

---
## **0. Navigating paths**
# **Navigating Directories and Working with Path Objects**

When working with files and directories, it is important to know how to navigate folders, create paths, and reference files in both **R** and **Python**.

---

## **01. Get Current Working Directory**

| Task | R Code | Python Code |
|------|--------|------------|
| **Print current working directory** | `getwd()` | `import os`<br>`print(os.getcwd())` |
| **Change working directory** | `setwd("path/to/folder")` | `os.chdir("path/to/folder")` |
| **Get absolute path of a file** | `normalizePath("data.csv")` | `import pathlib`<br>`print(pathlib.Path("data.csv").resolve())` |

---

## **02. Navigating Up and Down Directories**

| Task | R Code | Python Code |
|------|--------|------------|
| **Go up one directory** | `setwd("..")` | `os.chdir("..")` |
| **Go up two directories** | `setwd("../..")` | `os.chdir("../../")` |
| **Move into a subdirectory** | `setwd("subfolder")` | `os.chdir("subfolder")` |
| **Get parent directory** | `dirname(getwd())` | `print(pathlib.Path.cwd().parent)` |
| **Get grandparent directory** | `dirname(dirname(getwd()))` | `print(pathlib.Path.cwd().parent.parent)` |

---

## **03. Creating and Listing Files/Folders**

| Task | R Code | Python Code |
|------|--------|------------|
| **List files in directory** | `list.files()` | `os.listdir()` |
| **List files including hidden ones** | `list.files(all.files = TRUE)` | `os.listdir()` (hidden files start with `.`) |
| **List files recursively** | `list.files(recursive = TRUE)` | `import glob`<br>`files = glob.glob("**/*", recursive=True)` |
| **Create a new directory** | `dir.create("new_folder")` | `os.mkdir("new_folder")` |
| **Create nested directories** | `dir.create("parent/child", recursive = TRUE)` | `os.makedirs("parent/child", exist_ok=True)` |

---

## **04. Working with Paths Using `fs` and `pathlib`**

| Task | R Code (fs) | Python Code (pathlib) |
|------|------------|-----------------|
| **Create a path object** | `fs::path("data", "file.csv")` | `pathlib.Path("data") / "file.csv"` |
| **Check if a path exists** | `fs::file_exists("data/file.csv")` | `pathlib.Path("data/file.csv").exists()` |
| **Check if a path is a file** | `fs::file_exists("file.csv")` | `pathlib.Path("file.csv").is_file()` |
| **Check if a path is a directory** | `fs::dir_exists("folder")` | `pathlib.Path("folder").is_dir()` |
| **Get file extension** | `fs::path_ext("file.csv")` | `pathlib.Path("file.csv").suffix` |
| **Get filename without extension** | `fs::path_ext_remove("file.csv")` | `pathlib.Path("file.csv").stem` |
| **Get parent directory of a file** | `fs::path_dir("data/file.csv")` | `pathlib.Path("data/file.csv").parent` |

---

## **05. Deleting, Copying, and Moving Files**

| Task | R Code | Python Code |
|------|--------|------------|
| **Delete a file** | `file.remove("file.csv")` | `os.remove("file.csv")` |
| **Delete a directory** | `unlink("folder", recursive = TRUE)` | `import shutil`<br>`shutil.rmtree("folder")` |
| **Copy a file** | `file.copy("file.csv", "backup.csv")` | `shutil.copy("file.csv", "backup.csv")` |
| **Move (rename) a file** | `file.rename("old.csv", "new.csv")` | `os.rename("old.csv", "new.csv")` |

---

## **06. Finding Files by Pattern (Glob & Grep)**

| Task | R Code | Python Code |
|------|--------|------------|
| **Find all CSV files in a folder** | `list.files(pattern = "\\.csv$")` | `import glob`<br>`csv_files = glob.glob("*.csv")` |
| **Find files matching a pattern in subdirectories** | `list.files(recursive = TRUE, pattern = "\\.csv$")` | `csv_files = glob.glob("**/*.csv", recursive=True)` |
| **Find files with a specific prefix** | `list.files(pattern = "^data_.*\\.csv$")` | `csv_files = glob.glob("data_*.csv")` |
| **Find files containing "report" in name** | `list.files(pattern = "report")` | `csv_files = [f for f in os.listdir() if "report" in f]` |

---

---

## **1. Data Loading**

| Task | R Code | Python Code |
|------|--------|------------|
| **Read a CSV file** | `df <- read_csv("data.csv")` | `df = pd.read_csv("data.csv")` |
| **Read an Excel file** | `df <- readxl::read_excel("data.xlsx")` | `df = pd.read_excel("data.xlsx")` |
| **Read a Google Sheet** | `df <- read_sheet(ss = gs_id, sheet = "PHIA_GEO")` | `df = pd.read_csv("https://docs.google.com/spreadsheets/d/example.csv")` |
| **Read a JSON file** | `df <- jsonlite::fromJSON("data.json")` | `import json`<br>`df = pd.read_json("data.json")` |
| **Read a Parquet file** | `df <- arrow::read_parquet("data.parquet")` | `df = pd.read_parquet("data.parquet")` |
| **Read a Shapefile (GIS data)** | `df <- st_read("map.shp")` | `import geopandas as gpd`<br>`df = gpd.read_file("map.shp")` |

---

## **2. Data Filtering & Selection**

| Task | R Code | Python Code |
|------|--------|------------|
| **Filter rows where indicator == "TX_CURR"** | `df %>% filter(indicator == "TX_CURR")` | `df = df[df["indicator"] == "TX_CURR"]` |
| **Filter rows based on multiple conditions** | `df %>% filter(age > 30, gender == "Male")` | `df = df[(df["age"] > 30) & (df["gender"] == "Male")]` |
| **Select specific columns** | `df %>% select(name, age, gender)` | `df = df[["name", "age", "gender"]]` |
| **Drop a column** | `df %>% select(-age)` | `df = df.drop(columns=["age"])` |
| **Filter rows that do not contain a string** | `df %>% filter(!str_detect(name, "John"))` | `df = df[~df["name"].str.contains("John")]` |
| **Filter rows where values are in a list** | `df %>% filter(country %in% c("USA", "Canada"))` | `df = df[df["country"].isin(["USA", "Canada"])]` |

---

## **3. Grouping & Aggregation**

| Task | R Code | Python Code |
|------|--------|------------|
| **Sum values by group** | `df %>% group_by(state) %>% summarise(total = sum(sales))` | `df.groupby("state")["sales"].sum().reset_index()` |
| **Count occurrences of unique values** | `df %>% count(state)` | `df["state"].value_counts().reset_index()` |
| **Compute mean within groups** | `df %>% group_by(state) %>% summarise(avg_sales = mean(sales))` | `df.groupby("state")["sales"].mean().reset_index()` |
| **Compute multiple aggregations** | `df %>% group_by(state) %>% summarise(avg=mean(sales), total=sum(sales))` | `df.groupby("state")["sales"].agg(["mean", "sum"]).reset_index()` |
| **Rank within groups** | `df %>% group_by(state) %>% mutate(rank = rank(sales))` | `df["rank"] = df.groupby("state")["sales"].rank(method="first")` |
| **Cumulative sum within groups** | `df %>% group_by(state) %>% mutate(cumulative_sales = cumsum(sales))` | `df["cumulative_sales"] = df.groupby("state")["sales"].cumsum()` |

---

## **4. Joining & Reshaping Data**

| Task | R Code | Python Code |
|------|--------|------------|
| **Merge two datasets (left join)** | `df1 %>% left_join(df2, by="id")` | `df = df1.merge(df2, how="left", on="id")` |
| **Merge two datasets (inner join)** | `df1 %>% inner_join(df2, by="id")` | `df = df1.merge(df2, how="inner", on="id")` |
| **Convert wide to long format** | `df %>% pivot_longer(cols = starts_with("age"), names_to = "age_group", values_to = "value")` | `df.melt(id_vars=["id"], var_name="age_group", value_name="value")` |
| **Convert long to wide format** | `df %>% spread(key, value)` | `df.pivot(index="snu1", columns="funding_agency", values="n")` |
| **Drop duplicates** | `df %>% distinct()` | `df.drop_duplicates()` |
| **Concatenate multiple DataFrames** | `bind_rows(df1, df2)` | `pd.concat([df1, df2])` |

---

## **5. Creating & Modifying Columns**

| Task | R Code | Python Code |
|------|--------|------------|
| **Create a new column based on a condition** | `df %>% mutate(high_sales = if_else(sales > 1000, "Yes", "No"))` | `df["high_sales"] = np.where(df["sales"] > 1000, "Yes", "No")` |
| **Convert text to uppercase** | `df %>% mutate(name = toupper(name))` | `df["name"] = df["name"].str.upper()` |
| **Extract year from a date** | `df %>% mutate(year = year(date))` | `df["year"] = df["date"].dt.year` |
| **Extract month from a date** | `df %>% mutate(year = month(date))` | `df["year"] = df["date"].dt.month` |
| **Compute a percentage change** | `df %>% mutate(change = (sales / lag(sales)) - 1)` | `df["change"] = df["sales"].pct_change()` |
| **Apply a function to a column** | `df %>% mutate(price = price * 1.1)` | `df["price"] = df["price"].apply(lambda x: x * 1.1)` |
| **Fill missing values** | `df %>% replace_na(list(sales = 0))` | `df["sales"].fillna(0, inplace=True)` |

---

## **6. Visualization**

| Task | R Code (ggplot2) | Python Code (Matplotlib/Seaborn) |
|------|----------------|-----------------|
| **Bar chart** | `ggplot(df, aes(x = state, y = sales)) + geom_col()` | `plt.bar(df["state"], df["sales"])` |
| **Scatter plot** | `ggplot(df, aes(x = age, y = salary)) + geom_point()` | `plt.scatter(df["age"], df["salary"])` |
| **Line plot** | `ggplot(df, aes(x = date, y = sales)) + geom_line()` | `plt.plot(df["date"], df["sales"])` |
| **Box plot** | `ggplot(df, aes(x = state, y = sales)) + geom_boxplot()` | `sns.boxplot(x="state", y="sales", data=df)` |
| **Histogram** | `ggplot(df, aes(x = sales)) + geom_histogram()` | `plt.hist(df["sales"])` |
| **Facet plots** | `ggplot(df) + geom_histogram() + facet_wrap(~category)` | `sns.FacetGrid(df, col="category").map(plt.hist, "sales")` |

---

