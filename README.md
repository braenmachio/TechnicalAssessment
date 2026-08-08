## Technical Assessment Documentation

### 1. File Naming
- Python files are also treated as *modules* hence, lowercase separated by under_scores
`palindrome_checker.py` and `polymer_plant.py`

### 2. Minimal Dockerfile
- Be as small as reasonably possible. How do I accomplish this: 

**Multi stage the builds**

- Move dependecies from being compiled inside the runtime
- Build artifacts (.whl) are used for dependency installation at runtime   

**Runtime Codefiles**

- Copy only the required files by the application
**Test**
- `docker-compose.yaml` for a quick dry run :w
~~~
    psycopg version: 3.3.4
    Connecting with: host=db port=5432 dbname=postgres user=postgres password=postgres
    Connected successfully. Server says: PostgreSQL 16.14 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
~~~

**Conclusion**

- The multi-stage approach adds an **80MB** overhead on the base 26.04 in production compared to a single stage build with an overhead of **727 MB**
    
~~~
    comparison-singlestage:latest    7e7808b4106e        885MB          226MB
    postgres:16-alpine               57c72fd2a128        420MB          117MB    U
    technicalassessment-app:latest   483ef74ca405        238MB         60.5MB    U
    ubuntu:resolute                  678c6550cc43        158MB         45.3MB
~~~
**Notes**

- Only the runtime image suffices into production
- psycopg[c] being C optimized, during installation, C extensions shall be compiled.
- Add `build-essentials` & `python3-dev`
- What reruns? Any code layer that changes. `System Packages OR Dependencies OR InstructionFiles`

**Improvements**
  
- Pinning dependency version
- `.dockerignore` for host local env/secrets, dependecy directories, tests, IDE junk

### 2. Palindrome Checker
- Given that the there are no spaces or punctuation to strip, this meets the criteria for a slicing operation s == s[::-1]
- It's performant, however, the fact that it creates a copy of the sequence, it is less prefered in environments where memory is a constraining factor.

- In the code, I implement a `Two-Pointer pattern` for this operation thiswise:
1. A string passes for a sequence hence can be indexed and iterated over.
2. Using a pointer to look up indexes, I loop, comparatively, over the first and last items, inwardly.
    - if comparator returns a False, exit the loop. Not a palindrme
    - else
3. Loop inwards and compare the next items in the sequence (start+1, end-1)
4. If the loop fininshes without returning a mismatch, then the user input passes for a palindrome
~~~
%runfile /home/braen/Documents/TechnicalAssessment/palindrome_checker.py --wdir
>  kayak
True

%runfile /home/braen/Documents/TechnicalAssessment/palindrome_checker.py --wdir
>  racecars
False

%runfile /home/braen/Documents/TechnicalAssessment/palindrome_checker.py --wdir
>  racecar
True
~~~
