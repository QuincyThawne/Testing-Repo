# AIDS CTS TechRound Questions

---

### 1. **Introduction & Behavioral**
- Self introduction
- Internship explanation
- Projects in resume
- CTS project explanation
- Hackathon project explanation
- Certifications completed / explanation
- Strengths and weaknesses
- Preferred domain to work
- Flexible to work in any domain/location/shift
- Did you provide any bribe?
- Teamwork and behavioral scenarios
- How to approach learning new technology
- Managing longer working hours
- Availability for night shifts
- What do you know about Cognizant?

---

### 2. **Python Programming**
- Reverse a string/sentence/name
- Remove vowels from string
- Remove whitespaces in sentence
- Count whitespaces in sentence
- Print duplicates in list/duplicate identification
- Print common elements from two lists
- List creation: append(), insert()
- Convert list to tuple
- List vs tuple vs set
- Count words in sentence
- Find even/odd numbers from list
- Find max/min number from list
- Sort list (ascending/descending)
- Merge/reverse two lists
- Factorial using recursion
- Lambda functions
- Pattern problems
- Take input and print max/multiply by 10
- Check if number is prime
- Extract numbers from string and sum
- Generate random numbers
- Find missing element in array
- List addition
- Tuple vs list
- DSA types in Python
- Pandas, matplotlib (Python libraries)
- Packages/modules used in projects

---

### 3. **SQL & Database**
- Create table, insert data
- SQL string functions
- Remove specific letter from string
- Real-time examples of SQL usage
- Set operators
- Print a row twice even if only one entry exists
- Display day from date
- SQL query for 2nd/3rd highest salary
- Count of students/employees in each department
- Group by, order by, having, where clauses
- Window functions: row_number, rank, dense_rank
- Difference between inner join, left join, right join, cross join, outer join
- Write and explain all types of joins
- Print first_order and last_order date of a customer (aggregate functions)
- SQL query for employees between specific dates
- Subqueries
- SQL code for second highest salary
- Types of keys: primary, foreign, unique
- SQL set operators
- Limit in SQL

---

### 4. **Machine Learning & Data Science**
- ML models used in projects (XGBoost, LightGBM, Random Forest, CatBoost, Clustering, Regression)
- Difference between linear and logistic regression
- Supervised vs unsupervised learning
- Overfitting and underfitting
- Bias in ML
- Data preprocessing
- Model selection
- Accuracy metrics: precision, recall, mean squared error, performance metrics
- Scenario-based ML questions (which algorithms to use)
- Advantages/disadvantages of models
- Evaluation metrics and improving model frequency
- What is Generative AI?
- LLM (Large Language Models)
- Real-world use cases
- Types of regression
- Random forest vs clustering
- Decision tree vs random forest

---

### 5. **Cloud Computing & Related Technologies**
- What is cloud?
- Cloud experience
- Cloud services used (Azure, AWS, Databricks)
- Difference between on-premises and cloud services
- IaaS, PaaS, SaaS
- Cloud fundamentals
- Why Azure, why not other cloud?
- Other models available in cloud

---

### 6. **Other Technical Questions**
- OOPs concepts in Python
- Exception handling
- Difference between database and files
- Unstructured vs structured dataset (advantages/disadvantages)
- Gen AI models
- Time complexity for searching in list, tuple, set
- Private key, foreign key, unique key
- How industry works on inheritance concept in Java

---

### 7. **Aptitude & Miscellaneous**
- Ages ratio problem (A, B, C)
- General aptitude questions

---

### **Duplicates & Coverage**
- Many questions are repeated across panels (e.g., self intro, project explanation, flexible to work/shift/location, Python reverse string, SQL joins, ML models, cloud questions).
- Some questions are phrased differently but mean the same (e.g., “reverse a string” vs “write code to reverse your name”).
- All unique questions from all panels are present in your `.md` file.
- No major topic or question is missing.
- No unique question is excluded.

---

---

## Sample Answers to Common Interview Questions

---

### 1. **Introduction & Behavioral**

**Self introduction:**  
I am [Your Name], a recent graduate in [Your Major] with strong foundation in programming and data science. I have completed internships and projects that demonstrate my technical skills and passion for technology.

**Internship explanation:**  
During my internship at [Company], I worked on [specific project/task], where I gained hands-on experience in [technologies used] and contributed to [specific outcomes].

**Projects in resume:**  
My projects include [Project 1] using [Technology], [Project 2] involving [ML/Data Science], and [Project 3] showcasing [Web Development/Database]. Each project solved real-world problems and enhanced my technical skills.

**CTS hackathon project explanation:**  
In the CTS hackathon, I developed a [solution type] to address [problem statement]. I used [technologies/algorithms] and achieved [specific results/accuracy]. The project demonstrated my ability to work under pressure and deliver innovative solutions.

**Certifications completed:**  
I have completed certifications in [AWS/Azure/Python/Data Science], which validated my skills in [specific areas] and kept me updated with industry standards.

**Strengths and weaknesses:**  
My strengths include problem-solving, adaptability, and continuous learning. I'm working to improve my public speaking and presentation skills through practice and feedback.

**Flexible to work in any domain/location/shift:**  
Yes, I am completely flexible to work in any domain, location, or shift as required by the organization. I understand the global nature of IT services.

**Did you provide any bribe?:**  
No, I have never provided any bribe and believe in ethical practices and fair selection processes.

**Teamwork scenarios:**  
When team members face technical difficulties, I believe in collaborative problem-solving, knowledge sharing, and providing support to ensure project success.

---

### 2. **Python Programming**

**Reverse a string:**  
```python
# Method 1: Slicing
s = "hello"
print(s[::-1])  # Output: 'olleh'

# Method 2: Using loop
def reverse_string(s):
    return ''.join(reversed(s))
```

**Remove vowels from string:**  
```python
def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join([c for c in s if c not in vowels])

# Example
print(remove_vowels("hello world"))  # Output: "hll wrld"
```

**Convert uppercase to lowercase:**  
```python
s = "HELLO WORLD"
print(s.lower())  # Output: "hello world"
```

**Print duplicates in list:**  
```python
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)
```

**Print common elements from two lists:**  
```python
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(common)  # Output: [4, 5]
```

**GCD of two numbers:**  
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

**Factorial using recursion:**  
```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)
```

**Check if number is prime:**  
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

**Count whitespaces in sentence:**  
```python
def count_whitespaces(s):
    return s.count(' ')
```

**Remove whitespaces:**  
```python
def remove_whitespaces(s):
    return s.replace(' ', '')
```

**List vs Tuple vs Set:**  
- **List**: Mutable, ordered, allows duplicates `[1, 2, 3]`
- **Tuple**: Immutable, ordered, allows duplicates `(1, 2, 3)`
- **Set**: Mutable, unordered, no duplicates `{1, 2, 3}`

**Count words in sentence:**
```python
def count_words(sentence):
    return len(sentence.split())

# Example
print(count_words("Hello world Python"))  # Output: 3
```

**Find max/min from list:**
```python
numbers = [1, 5, 3, 9, 2]
print(max(numbers))  # Output: 9
print(min(numbers))  # Output: 1
```

**Sort list:**
```python
numbers = [3, 1, 4, 1, 5]
numbers.sort()  # Ascending: [1, 1, 3, 4, 5]
numbers.sort(reverse=True)  # Descending: [5, 4, 3, 1, 1]
```

**Merge two lists:**
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2  # [1, 2, 3, 4, 5, 6]
```

**Lambda functions:**
```python
# Square function
square = lambda x: x**2
print(square(5))  # Output: 25

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

**Pattern problems:**
```python
# Print triangle pattern
def triangle_pattern(n):
    for i in range(1, n+1):
        print('*' * i)

# Print number pattern
def number_pattern(n):
    for i in range(1, n+1):
        print(' '.join(str(j) for j in range(1, i+1)))
```

**Extract numbers from string and sum:**
```python
import re
def sum_numbers_in_string(s):
    numbers = re.findall(r'\d+', s)
    return sum(int(num) for num in numbers)

# Example
print(sum_numbers_in_string("abc123def456"))  # Output: 579
```

**Generate random numbers:**
```python
import random
# Random integer between 1 and 10
print(random.randint(1, 10))

# Random float between 0 and 1
print(random.random())

# Random choice from list
print(random.choice([1, 2, 3, 4, 5]))
```

**Find missing element in array:**
```python
def find_missing(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example: [1, 2, 4, 5] missing 3
print(find_missing([1, 2, 4, 5], 5))  # Output: 3
```

**List operations:**
```python
# Append and Insert
lst = [1, 2, 3]
lst.append(4)       # [1, 2, 3, 4]
lst.insert(1, 10)   # [1, 10, 2, 3, 4]

# Remove element
lst.remove(10)      # [1, 2, 3, 4]
lst.pop()          # [1, 2, 3]
```

**Convert list to tuple:**
```python
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (1, 2, 3, 4)
```

**DSA types in Python:**
- **Lists**: Dynamic arrays `[1, 2, 3]`
- **Tuples**: Immutable sequences `(1, 2, 3)`
- **Sets**: Hash tables `{1, 2, 3}`
- **Dictionaries**: Hash maps `{"a": 1, "b": 2}`
- **Queues**: `collections.deque`
- **Stacks**: Using lists with append/pop

---

### 3. **SQL & Database**

**Create table and insert data:**  
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    dept_id INT,
    hire_date DATE
);

INSERT INTO employees VALUES (1, 'Alice', 50000, 1, '2020-01-15');
```

**Types of Joins:**  
```sql
-- INNER JOIN: Common records
SELECT e.name, d.dept_name 
FROM employees e INNER JOIN departments d ON e.dept_id = d.id;

-- LEFT JOIN: All from left table
SELECT e.name, d.dept_name 
FROM employees e LEFT JOIN departments d ON e.dept_id = d.id;

-- RIGHT JOIN: All from right table
SELECT e.name, d.dept_name 
FROM employees e RIGHT JOIN departments d ON e.dept_id = d.id;

-- FULL OUTER JOIN: All records from both tables
SELECT e.name, d.dept_name 
FROM employees e FULL OUTER JOIN departments d ON e.dept_id = d.id;
```

**Window Functions - ROW_NUMBER, RANK, DENSE_RANK:**  
```sql
-- ROW_NUMBER: Sequential numbering
SELECT name, salary, ROW_NUMBER() OVER (ORDER BY salary DESC) as rn
FROM employees;

-- RANK: Same rank for ties, gaps in sequence
SELECT name, salary, RANK() OVER (ORDER BY salary DESC) as rank
FROM employees;

-- DENSE_RANK: Same rank for ties, no gaps
SELECT name, salary, DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank
FROM employees;
```

**Find 2nd highest salary:**  
```sql
SELECT MAX(salary) as second_highest
FROM employees 
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Using LIMIT
SELECT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;
```

**Group By and Having:**  
```sql
SELECT dept_id, COUNT(*) as emp_count, AVG(salary) as avg_salary
FROM employees 
GROUP BY dept_id
HAVING COUNT(*) > 2;
```

**Display day from date:**  
```sql
SELECT DAYNAME(hire_date) as day_name FROM employees;
-- OR
SELECT EXTRACT(DAY FROM hire_date) as day_number FROM employees;
```

**Date range query:**  
```sql
SELECT * FROM employees 
WHERE hire_date BETWEEN '2015-01-01' AND '2020-12-31';
```

---

### 4. **Machine Learning & Data Science**

**Difference between XGBoost and LightGBM:**  
- **XGBoost**: Gradient boosting, high accuracy, slower training
- **LightGBM**: Light gradient boosting, faster training, less memory usage

**Linear vs Logistic Regression:**  
- **Linear**: Predicts continuous values, uses least squares
- **Logistic**: Predicts probabilities/categories, uses sigmoid function

**Precision and Recall:**  
- **Precision**: TP/(TP+FP) - How many predicted positives are actually positive
- **Recall**: TP/(TP+FN) - How many actual positives were correctly identified

**Overfitting and Underfitting:**  
- **Overfitting**: Model memorizes training data, poor generalization
- **Underfitting**: Model too simple, poor performance on both training and test data

**Supervised vs Unsupervised Learning:**  
- **Supervised**: Uses labeled data (classification, regression)
- **Unsupervised**: Uses unlabeled data (clustering, dimensionality reduction)

**What is bias in ML:**  
Bias is the error from oversimplifying assumptions in the learning algorithm. High bias can cause underfitting.

**Random Forest vs Decision Tree:**  
- **Decision Tree**: Single tree, prone to overfitting
- **Random Forest**: Ensemble of trees, reduces overfitting, better accuracy

**What is Generative AI:**  
AI that creates new content (text, images, code) based on training data. Examples: GPT, DALL-E, ChatGPT.

---

### 5. **Cloud Computing & Related Technologies**

**What is cloud computing:**  
Cloud computing delivers computing services (servers, storage, databases, software) over the internet, enabling on-demand access and scalability.

**Advantages of cloud over local server:**  
- Scalability and flexibility
- Cost-effectiveness (pay-as-you-use)
- Global accessibility
- Automatic updates and maintenance
- Disaster recovery and backup

**IaaS, PaaS, SaaS:**  
- **IaaS**: Infrastructure (AWS EC2, Azure VMs)
- **PaaS**: Platform for development (AWS Lambda, Azure App Service)
- **SaaS**: Ready-to-use software (Office 365, Gmail)

**About AWS:**  
Amazon Web Services is a comprehensive cloud platform offering 200+ services including compute, storage, databases, and AI/ML tools.

**S3 Buckets:**  
Simple Storage Service containers for storing objects (files) in the cloud with high durability and availability.

**Databricks:**  
Unified analytics platform for big data and machine learning, built on Apache Spark.

---

### 6. **Other Technical Questions**

**OOPs concepts in Python:**  
- **Encapsulation**: Bundling data and methods
- **Inheritance**: Creating new classes based on existing ones
- **Polymorphism**: Same interface, different implementations
- **Abstraction**: Hiding complex implementation details

**Exception handling:**  
```python
try:
    # risky code
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"General error: {e}")
finally:
    print("Cleanup code")
```

**Structured vs Unstructured data:**  
- **Structured**: Organized format (databases, CSV) - easy to query, analyze
- **Unstructured**: No predefined format (text, images, videos) - flexible but harder to process

**Time complexity:**  
- **List**: O(n) for search, O(1) for access by index
- **Tuple**: O(n) for search, O(1) for access by index  
- **Set**: O(1) average for search, add, remove

---

### 7. **Behavioral & Scenario Questions**

**Challenges faced in projects:**  
I faced data quality issues in my ML project. I resolved it by implementing data cleaning techniques, handling missing values, and validating data sources.

**Team collaboration:**  
When team members face technical difficulties, I organize knowledge-sharing sessions, provide code reviews, and ensure clear documentation for better collaboration.

**Learning new technology:**  
I start with official documentation, take online courses, practice with small projects, and join community forums for support and best practices.

---
