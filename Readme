## Technical Assessment Documentation

### 1. File Naming
_ Python files are also treated as *modules* hence, lowercase separated by under_scores
`palindrome_checker.py` and `polymer_plant.py`

### 2. Minimal Dockerfile
_ Be as small as reasonably possible. How do I accomplish this: 

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

- The multi-stage approach adds an **80MB** overhead on the base 26.04 in production vs. to a single stage build with an overhead of **727 MB**
    
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
