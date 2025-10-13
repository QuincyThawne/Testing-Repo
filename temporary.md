# Python Practice Programs
---

### 1. Check for Palindrome

```python
s = input("Enter a string: ")
print("Palindrome" if s == s[::-1] else "Not Palindrome")
```

---

### 2. Factorial of a Number

```python
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

n = int(input("Enter number: "))
print("Factorial:", factorial(n))
```

---

### 3. Fibonacci Series

```python
n = int(input("Enter terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

---

### 4. Count Vowels in a String

```python
s = input("Enter string: ").lower()
vowels = "aeiou"
count = sum(1 for ch in s if ch in vowels)
print("Vowel count:", count)
```

---

### 5. Reverse a Number

```python
n = int(input("Enter number: "))
print("Reversed:", int(str(n)[::-1]))
```

---

### 6. Anagram Check

```python
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print("Anagram" if sorted(s1) == sorted(s2) else "Not Anagram")
```

---

### 7. Prime Number Check

```python
n = int(input("Enter number: "))
print("Prime" if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1)) else "Not Prime")
```

---

### 8. Second Largest Element

```python
arr = list(map(int, input("Enter numbers: ").split()))
uniq = sorted(set(arr))
print("Second largest:", uniq[-2])
```

---

### 9. Find Duplicate Elements

```python
arr = list(map(int, input("Enter numbers: ").split()))
duplicates = set([x for x in arr if arr.count(x) > 1])
print("Duplicates:", duplicates)
```

---

### 10. Sum of Digits

```python
n = int(input("Enter number: "))
print("Sum of digits:", sum(map(int, str(n))))
```

---

### 11. Armstrong Number Check

```python
n = int(input("Enter number: "))
s = sum(int(d)**len(str(n)) for d in str(n))
print("Armstrong" if n == s else "Not Armstrong")
```

---

### 12. Balanced Parentheses

```python
def is_balanced(s):
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

s = input("Enter expression: ")
print("Balanced" if is_balanced(s) else "Not Balanced")
```

---

### 13. String Compression (Run-Length Encoding)

```python
s = input("Enter string: ")
res, count = "", 1
for i in range(1, len(s)+1):
    if i < len(s) and s[i] == s[i-1]:
        count += 1
    else:
        res += s[i-1] + str(count)
        count = 1
print("Compressed:", res)
```

---

### 14. Find Missing Number in a List

```python
arr = list(map(int, input("Enter numbers: ").split()))
n = len(arr) + 1
expected_sum = n * (n + 1) // 2
print("Missing number:", expected_sum - sum(arr))
```

---

### 15. Star Pattern - Pyramid

```python
n = int(input("Rows: "))
for i in range(n):
    print(" "*(n-i-1) + "*"*(2*i+1))
```

---

### 16. Inverted Pyramid Pattern

```python
n = int(input("Rows: "))
for i in range(n, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))
```

---

### 17. Right-Angled Triangle Number Pattern

```python
n = int(input("Rows: "))
for i in range(1, n+1):
    print(" ".join(str(j) for j in range(1, i+1)))
```

---

### 18. Diamond Star Pattern

```python
n = int(input("Rows: "))
for i in range(n):
    print(" "*(n-i-1) + "*"*(2*i+1))
for i in range(n-2, -1, -1):
    print(" "*(n-i-1) + "*"*(2*i+1))
```

---

### 19. Pascal’s Triangle

```python
from math import comb
n = int(input("Rows: "))
for i in range(n):
    print(" "*(n-i), end="")
    print(" ".join(str(comb(i, k)) for k in range(i+1)))
```

---

### 20. Hollow Square Pattern

```python
n = int(input("Size: "))
for i in range(n):
    for j in range(n):
        if i in (0, n-1) or j in (0, n-1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

---

### 21. Reverse Words in a Sentence

```python
s = input("Enter sentence: ")
print(" ".join(s.split()[::-1]))
```

---

### 22. Remove Duplicates from String

```python
s = input("Enter string: ")
res = ""
for ch in s:
    if ch not in res:
        res += ch
print("Without duplicates:", res)
```

---

### 23. Find the Longest Word

```python
s = input("Enter sentence: ").split()
print("Longest word:", max(s, key=len))
```

---

### 24. Count Frequency of Each Character

```python
s = input("Enter string: ")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
```

---

### 25. Replace Spaces with Hyphens

```python
s = input("Enter string: ")
print(s.replace(" ", "-"))
```

---

# Additional Questions

---

# 🔹 Sorting & Searching

### 1. Bubble Sort

```python
arr = [5, 2, 9, 1, 5, 6]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Bubble Sort:", arr)
```

---

### 2. Selection Sort

```python
arr = [64, 25, 12, 22, 11]
for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print("Selection Sort:", arr)
```

---

### 3. Insertion Sort

```python
arr = [12, 11, 13, 5, 6]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
print("Insertion Sort:", arr)
```

---

### 4. Binary Search

```python
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 3, 5, 7, 9]
print("Index:", binary_search(arr, 7))
```

---

# 🔹 Matrix Problems

### 5. Transpose of a Matrix

```python
mat = [[1,2,3],[4,5,6],[7,8,9]]
transpose = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
print("Transpose:", transpose)
```

---

### 6. Print Diagonals

```python
mat = [[1,2,3],[4,5,6],[7,8,9]]
print("Primary diagonal:", [mat[i][i] for i in range(len(mat))])
print("Secondary diagonal:", [mat[i][len(mat)-i-1] for i in range(len(mat))])
```

---

### 7. Rotate Matrix 90°

```python
mat = [[1,2,3],[4,5,6],[7,8,9]]
rotated = list(zip(*mat[::-1]))
print("Rotated 90°:", rotated)
```

---

# 🔹 String Manipulation

### 8. Check Rotation

```python
s1, s2 = "abcde", "cdeab"
print("Rotation" if len(s1)==len(s2) and s2 in s1+s1 else "Not Rotation")
```

---

### 9. Longest Palindrome Substring (brute force)

```python
def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            temp = s[i:j+1]
            if temp == temp[::-1] and len(temp) > len(res):
                res = temp
    return res

print("Longest Palindrome:", longest_palindrome("babad"))
```

---

### 10. Remove Special Characters

```python
import re
s = "he@llo! wo#rld123"
print(re.sub(r'[^a-zA-Z0-9 ]', '', s))
```

---

# 🔹 Array / List Problems

### 11. Majority Element

```python
arr = [3,3,4,2,4,4,2,4,4]
print("Majority element:", max(set(arr), key=arr.count))
```

---

### 12. Kadane’s Algorithm

```python
arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum, curr_sum = arr[0], 0
for x in arr:
    curr_sum = max(x, curr_sum + x)
    max_sum = max(max_sum, curr_sum)
print("Max Subarray Sum:", max_sum)
```

---

### 13. Move Zeros to End

```python
arr = [0,1,0,3,12]
res = [x for x in arr if x != 0] + [0]*arr.count(0)
print("After moving zeros:", res)
```

---

### 14. Merge Two Sorted Arrays

```python
a, b = [1,3,5], [2,4,6]
merged = sorted(a+b)
print("Merged:", merged)
```

---

# 🔹 Stack & Queue

### 15. Stack using List

```python
stack = []
stack.append(10)
stack.append(20)
print(stack.pop())  # 20
```

---

### 16. Queue using Deque

```python
from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
print(queue.popleft())  # 10
```

---

# 🔹 Recursion

### 17. GCD (Euclidean)

```python
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

print("GCD:", gcd(56, 98))
```

---

### 18. Tower of Hanoi

```python
def hanoi(n, source, target, aux):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n-1, source, aux, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n-1, aux, target, source)

hanoi(3, 'A', 'C', 'B')
```

---

### 19. Generate Subsets

```python
def subsets(nums):
    res = [[]]
    for num in nums:
        res += [x+[num] for x in res]
    return res

print("Subsets:", subsets([1,2,3]))
```

---

# 🔹 Hashing Problems

### 20. Two-Sum

```python
arr, target = [2,7,11,15], 9
seen = {}
for i, num in enumerate(arr):
    if target-num in seen:
        print("Indices:", (seen[target-num], i))
    seen[num] = i
```

---

### 21. Subarray with Given Sum

```python
arr, target = [1,4,20,3,10,5], 33
s, curr_sum = 0, 0
for e in range(len(arr)):
    curr_sum += arr[e]
    while curr_sum > target:
        curr_sum -= arr[s]
        s += 1
    if curr_sum == target:
        print("Subarray:", arr[s:e+1])
        break
```

---

```Typescript

import { useEffect, useState } from "react";
import { useAuth } from "@/contexts/AuthContext";
import DashboardLayout from "@/components/DashboardLayout";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { supabase } from "@/integrations/supabase/client";
import { BookOpen, Plus, Users, Calendar } from "lucide-react";
import { Link } from "react-router-dom";
import { toast } from "sonner";

interface Course {
  id: string;
  title: string;
  description: string;
  code: string;
  campus: string;
}

interface Enrollment {
  id: string;
  course_id: string;
  courses: Course;
}

interface GreenLeaderboardRow {
  user_id: string;
  total_points: number;
  profiles: {
    full_name: string | null;
  } | null;
}

const Dashboard = () => {
  const { profile } = useAuth();
  const [enrolledCourses, setEnrolledCourses] = useState<Enrollment[]>([]);
  const [createdCourses, setCreatedCourses] = useState<Course[]>([]);
  const [availableCourses, setAvailableCourses] = useState<Course[]>([]);
  const [loading, setLoading] = useState(true);
  const [greenPoints, setGreenPoints] = useState(0);
  const [greenLeaderboard, setGreenLeaderboard] = useState<GreenLeaderboardRow[]>([]);
  const [upcomingOrders, setUpcomingOrders] = useState<number>(0);
  const [dueBooks, setDueBooks] = useState<number>(0);

  useEffect(() => {
    loadDashboardData();
  }, [profile]);

  const loadDashboardData = async () => {
    if (!profile) return;

    try {
      if (profile.role === "student") {
        // Load enrolled courses
        const { data: enrollments, error: enrollError } = await supabase
          .from("enrollments")
          .select("*, courses(*)")
          .eq("student_id", profile.id);

        if (enrollError) throw enrollError;
        setEnrolledCourses(enrollments || []);

        // Load available courses
        const enrolledIds = enrollments?.map(e => e.course_id) || [];
        
        let availableQuery = supabase
          .from("courses")
          .select("*");
        
        // Only filter out enrolled courses if there are any
        if (enrolledIds.length > 0) {
          availableQuery = availableQuery.not("id", "in", `(${enrolledIds.join(",")})`);
        }
        
        const { data: available, error: availError } = await availableQuery.limit(6);

        if (availError) throw availError;
        setAvailableCourses(available || []);
      } else if (profile.role === "faculty") {
        // Load created courses
        const { data: courses, error } = await supabase
          .from("courses")
          .select("*")
          .eq("faculty_id", profile.id);

        if (error) throw error;
        setCreatedCourses(courses || []);
      }

      // Sustainability quick stats
      const [{ data: actions }, { data: leaderboard }] = await Promise.all([
        supabase
          .from("campus_green_actions")
          .select("points")
          .eq("user_id", profile.id),
        supabase
          .from("campus_green_actions")
          .select("user_id, points, profiles(full_name)")
          .order("points", { ascending: false }),
      ]);

      const totalPoints = (actions || []).reduce(
        (acc, row) => acc + Number(row.points ?? 0),
        0
      );
      setGreenPoints(totalPoints);

      const leaderboardMap = new Map<string, GreenLeaderboardRow>();
      (leaderboard || []).forEach((row: any) => {
        const current = leaderboardMap.get(row.user_id);
        const points = Number(row.points ?? 0);
        if (current) {
          current.total_points += points;
        } else {
          leaderboardMap.set(row.user_id, {
            user_id: row.user_id,
            total_points: points,
            profiles: row.profiles,
          });
        }
      });
      setGreenLeaderboard(
        Array.from(leaderboardMap.values())
          .sort((a, b) => b.total_points - a.total_points)
          .slice(0, 3)
      );

      // Campus life reminders
      if (profile.role === "student") {
        const [{ data: upcoming }, { data: fines }] = await Promise.all([
          supabase
            .from("canteen_orders")
            .select("id")
            .eq("user_id", profile.id)
            .in("status", ["pending", "preparing", "ready"]),
          supabase
            .from("borrow_records")
            .select("id")
            .eq("user_id", profile.id)
            .eq("status", "overdue"),
        ]);
        setUpcomingOrders(upcoming?.length || 0);
        setDueBooks(fines?.length || 0);
      }
    } catch (error: any) {
      console.error("Dashboard loading error:", error);
      toast.error(error.message || "Failed to load dashboard data");
    } finally {
      setLoading(false);
    }
  };

  const enrollInCourse = async (courseId: string) => {
    try {
      const { error } = await supabase.from("enrollments").insert({
        course_id: courseId,
        student_id: profile?.id,
      });

      if (error) throw error;
      toast.success("Enrolled successfully!");
      loadDashboardData();
    } catch (error: any) {
      toast.error(error.message || "Failed to enroll");
    }
  };

  if (loading) {
    return (
      <DashboardLayout>
        <div className="flex items-center justify-center h-96">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary mx-auto mb-4"></div>
            <p className="text-muted-foreground">Loading your dashboard...</p>
          </div>
        </div>
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout>
      <div className="space-y-8">
        {/* Welcome Section */}
        <div className="relative overflow-hidden rounded-2xl bg-gradient-to-br from-primary via-primary to-accent p-8 text-primary-foreground shadow-hard">
          <div className="relative z-10">
            <h1 className="text-3xl font-bold mb-2">
              Welcome back, {profile?.full_name || "User"}!
            </h1>
            <p className="text-primary-foreground/90 text-lg">
              {profile?.role === "student" && "Ready to continue your learning journey?"}
              {profile?.role === "faculty" && "Manage your courses and inspire students."}
              {profile?.role === "librarian" && "Manage library resources and help students."}
              {profile?.role === "canteen_staff" && "Manage orders and keep the campus fed!"}
              {profile?.role === "admin" && "Oversee the entire campus ecosystem."}
            </p>
          </div>
          <div className="absolute right-0 top-0 h-full w-1/3 opacity-10">
            <BookOpen className="h-full w-full" />
          </div>
        </div>

        {/* Student View */}
        {profile?.role === "student" && (
          <>
            {/* My Courses - Featured Section */}
            <div>
              <div className="flex items-center justify-between mb-6">
                <div>
                  <h2 className="text-2xl font-bold flex items-center gap-2">
                    <BookOpen className="h-7 w-7 text-primary" />
                    My Courses
                  </h2>
                  <p className="text-muted-foreground text-sm mt-1">
                    {enrolledCourses.length === 0 
                      ? "Enroll in courses to start learning" 
                      : `You're enrolled in ${enrolledCourses.length} course${enrolledCourses.length !== 1 ? 's' : ''}`}
                  </p>
                </div>
                <Button asChild>
                  <Link to="/courses">
                    <Plus className="mr-2 h-4 w-4" />
                    Browse Courses
                  </Link>
                </Button>
              </div>
              {enrolledCourses.length === 0 ? (
                <Card className="shadow-soft border-dashed">
                  <CardContent className="flex flex-col items-center justify-center py-12">
                    <div className="rounded-full bg-primary/10 p-4 mb-4">
                      <BookOpen className="h-12 w-12 text-primary" />
                    </div>
                    <h3 className="font-semibold text-lg mb-2">No Courses Yet</h3>
                    <p className="text-muted-foreground text-center mb-4 max-w-md">
                      You haven't enrolled in any courses yet. Browse available courses below and start your learning journey!
                    </p>
                    <Button asChild size="lg">
                      <Link to="/courses">
                        <Plus className="mr-2 h-4 w-4" />
                        Explore Courses
                      </Link>
                    </Button>
                  </CardContent>
                </Card>
              ) : (
                <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                  {enrolledCourses.map((enrollment) => (
                    <Card key={enrollment.id} className="hover:shadow-medium transition-all hover:scale-[1.02] border-2">
                      <CardHeader className="pb-3">
                        <div className="flex items-start justify-between mb-2">
                          <Badge variant="secondary" className="font-mono">{enrollment.courses.code}</Badge>
                          <Badge variant="outline" className="text-xs">{enrollment.courses.campus}</Badge>
                        </div>
                        <CardTitle className="text-lg leading-tight">{enrollment.courses.title}</CardTitle>
                        <CardDescription className="line-clamp-2 text-sm">
                          {enrollment.courses.description}
                        </CardDescription>
                      </CardHeader>
                      <CardContent className="space-y-2">
                        <Button asChild className="w-full" size="sm">
                          <Link to={`/courses/${enrollment.courses.id}`}>
                            <BookOpen className="mr-2 h-4 w-4" />
                            Open Course
                          </Link>
                        </Button>
                      </CardContent>
                    </Card>
                  ))}
                </div>
              )}
            </div>

            {/* Available Courses */}
            {availableCourses.length > 0 && (
              <div>
                <h2 className="text-2xl font-bold mb-4">Available Courses</h2>
                <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                  {availableCourses.map((course) => (
                    <Card key={course.id} className="hover:shadow-medium transition-shadow">
                      <CardHeader>
                        <Badge variant="outline" className="w-fit">{course.code}</Badge>
                        <CardTitle className="text-lg">{course.title}</CardTitle>
                        <CardDescription className="line-clamp-2">
                          {course.description}
                        </CardDescription>
                      </CardHeader>
                      <CardContent>
                        <Button
                          onClick={() => enrollInCourse(course.id)}
                          variant="outline"
                          className="w-full"
                        >
                          <Plus className="mr-2 h-4 w-4" />
                          Enroll Now
                        </Button>
                      </CardContent>
                    </Card>
                  ))}
                </div>
              </div>
            )}
          </>
        )}

        {/* Faculty View */}
        {profile?.role === "faculty" && (
          <div>
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-2xl font-bold">My Courses</h2>
              <Button asChild>
                <Link to="/courses/create">
                  <Plus className="mr-2 h-4 w-4" />
                  Create Course
                </Link>
              </Button>
            </div>
            {createdCourses.length === 0 ? (
              <Card className="shadow-soft">
                <CardContent className="flex flex-col items-center justify-center py-12">
                  <BookOpen className="h-12 w-12 text-muted-foreground mb-4" />
                  <p className="text-muted-foreground text-center mb-4">
                    You haven't created any courses yet.
                  </p>
                  <Button asChild>
                    <Link to="/courses/create">
                      <Plus className="mr-2 h-4 w-4" />
                      Create Your First Course
                    </Link>
                  </Button>
                </CardContent>
              </Card>
            ) : (
              <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                {createdCourses.map((course) => (
                  <Card key={course.id} className="hover:shadow-medium transition-shadow">
                    <CardHeader>
                      <div className="flex items-start justify-between">
                        <Badge variant="secondary">{course.code}</Badge>
                      </div>
                      <CardTitle className="text-lg">{course.title}</CardTitle>
                      <CardDescription className="line-clamp-2">
                        {course.description}
                      </CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-2">
                      <Button asChild className="w-full">
                        <Link to={`/courses/${course.id}`}>Manage Course</Link>
                      </Button>
                    </CardContent>
                  </Card>
                ))}
              </div>
            )}
          </div>
        )}

        {/* Quick Stats */}
        <div className="grid gap-4 md:grid-cols-3">
          <Card className="shadow-soft">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <CardTitle className="text-sm font-medium">Total Courses</CardTitle>
              <BookOpen className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">
                {profile?.role === "student" ? enrolledCourses.length : createdCourses.length}
              </div>
            </CardContent>
          </Card>
          <Card className="shadow-soft">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <CardTitle className="text-sm font-medium">Active This Week</CardTitle>
              <Calendar className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{profile?.role === "student" ? upcomingOrders : greenLeaderboard.length}</div>
              <p className="text-xs text-muted-foreground">
                {profile?.role === "student"
                  ? "Orders & pickups awaiting action"
                  : "Peers leading sustainability scores"}
              </p>
            </CardContent>
          </Card>
          <Card className="shadow-soft">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <CardTitle className="text-sm font-medium">Campus Community</CardTitle>
              <Users className="h-4 w-4 text-muted-foreground" />
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">{profile?.campus}</div>
              <p className="text-xs text-muted-foreground">Green points earned: {greenPoints}</p>
            </CardContent>
          </Card>
        </div>

        <Card className="shadow-soft">
          <CardHeader>
            <CardTitle>Eco Leaders Spotlight</CardTitle>
            <CardDescription>Cheer on campuses making sustainability a habit</CardDescription>
          </CardHeader>
          <CardContent className="grid gap-4 md:grid-cols-3">
            {greenLeaderboard.length === 0 ? (
              <p className="text-sm text-muted-foreground">
                Log your first action in the Green Impact Lab to appear here.
              </p>
            ) : (
              greenLeaderboard.map((entry, index) => (
                <div key={entry.user_id} className="rounded-xl border p-4">
                  <p className="text-xs text-muted-foreground">#{index + 1}</p>
                  <p className="font-semibold">
                    {entry.profiles?.full_name || "Student"}
                  </p>
                  <p className="text-xs text-muted-foreground">{entry.total_points} pts</p>
                </div>
              ))
            )}
          </CardContent>
        </Card>
      </div>
    </DashboardLayout>
  );
};

export default Dashboard;
```
