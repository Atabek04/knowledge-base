1. Build project :luc_arrow_right: `myapp.ear` or `myapp.jar` (no server inside)
2. Cannot run standalone - must deploy to application server
3. Deploy :luc_arrow_right: Copy to EJB Container (WebLogic, JBoss etc.) server deployment folder
4. Server unpacks your code, wraps it with container services (transactions, concurrency etc.), managed its lifecycle

> The container is a long-running process (like Tomcat)
> that you deploy into it.

---

## Testing on localhost with EJB

1. Download JBoss/WebLogic (hundreds of MBs)
2. **Start the server** → `./startWebLogic.sh` (runs on port 7001, 8080, etc.)
3. **Deploy your EAR/JAR** → copy to `deployments/` folder or use admin console
4. **Test** → hit `http://localhost:8080/yourapp/endpoint`

The server process **must be running**
It's like having Tomcat running,
	but much heavier (EJB servers consume 500MB-2GB memory just to start).

---

## Deployment differences: Now vs EJB

#### Docker/Modern

- Your `JAR` c**ontains everything** (app code + embedded Tomcat + libraries)
- Docker image = OS + JVM + your fat JAR
- Run anywhere, self-contained

#### EJB

- Your `EAR`/`JAR` **contains only** business code + EJB interfaces implementation
- Application server **already running** with all infrastructure
- Your code **plugs into** the server's existing services

#### Before EJB

- Build your project, copy `JAR` to server, run `java -cp myapp.jar com.company.Main`
- No standardized services :luc_arrow_right: each company's setup different
- Manual scaling :luc_arrow_right: modify code to handle threading

#### Key difference:

Modern = you bring the runtime with you
EJB = runtime already running, you just plug your business logic
