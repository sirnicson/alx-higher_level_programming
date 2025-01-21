# Python - Network #0

A collection of Bash scripts and a Python program for interacting with HTTP servers.

## Tasks

### Bash Scripts
1. **0-body_size.sh**  
   Sends a GET request to a URL and displays the size of the response body (in bytes).

2. **1-body.sh**  
   Sends a GET request to a URL and displays the response body for a 200 status code.

3. **2-delete.sh**  
   Sends a DELETE request to a URL and displays the response body.

4. **3-methods.sh**  
   Displays all HTTP methods the server of a given URL will accept.

5. **4-header.sh**  
   Sends a GET request with a header `X-School-User-Id=98` and displays the response body.

6. **5-post_params.sh**  
   Sends a POST request with `email=test@gmail.com` and `subject=I will always be here for PLD`.

7. **100-status_code.sh**  
   Sends a GET request and displays the status code without using pipes, redirections, `;`, or `&&`.

8. **101-post_json.sh**  
   Sends a JSON POST request with a file's contents and displays the response body.

9. **102-catch_me.sh**  
   Sends a request to `0.0.0.0:5000/catch_me` to get the response `You got me!`.

### Python Program
- **6-peak.py**  
   Finds a peak in a list of unsorted integers.  
   - **6-peak.txt**: Contains the algorithm's complexity.

# Tests
Test files are provided in the `tests` folder.

