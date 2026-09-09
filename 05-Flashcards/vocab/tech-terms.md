TARGET DECK: English::Tech Terms

START
English Card
to impute
Back: To **calculate or estimate a missing value** by comparing it to similar known values.
- In ML/statistics: filling in missing data by mean, median, KNN and the like
- General English means to attribute blame or credit to someone
Russian: вменять; подставлять (пропущенные значения)
Example: Before training the model, we **imputed** missing ages using the column's median value.
Tags: vocab ml data-preprocessing statistics
<!--ID: 1788671819588-->
END

START
English Card
bias
Back: A tendency to **support or oppose something unfairly**, driven by personal opinion rather than facts.
Russian: предубеждение; пристрастие
Example: Hiring decisions can reflect **bias** if interviewers favor candidates from their own background.
Tags: vocab general
<!--ID: 1788671819604-->
END

START
English Card
biased model
Back: A model that learns a **distorted version of reality** because its training data didn't represent the full picture.
- Not the technical bias term in `y = wx + b` — this is a systematic blind spot from unrepresentative data
Russian: смещённая модель; модель с предвзятостью
Example: High-income people skipped the income field, so after dropping those rows the **biased model** predicted everyone earns less.
Tags: vocab ml data-preprocessing
<!--ID: 1788671819614-->
END

START
English Card
outlier
Back: A data point **very different from the rest**, so it cannot be used to draw general conclusions.
Russian: выброс; аномальное значение
Example: People who live past 100 are genetic **outliers**, whose longevity is unreachable for most of us.
Tags: vocab statistics ml
<!--ID: 1788671819617-->
END

START
English Card
categorical column
Back: A column holding a **limited set of distinct labels or groups** rather than numbers.
- Most ML algorithms need it converted to numbers first (one-hot or label encoding)
Russian: категориальный столбец
Example: The "Gender" and "City" columns are **categorical columns** — they hold text labels like "Male" or "London", not numeric values.
Tags: vocab ml data-preprocessing
<!--ID: 1788671819621-->
END

START
English Card
seed
Back: A **fixed starting number for a random number generator (RNG)** that makes it produce the same sequence of "random" results every run.
Russian: начальное значение (генератора случайных чисел)
Example: Setting `random_state=42` provides a **seed** so the train-test split is identical every run.
Tags: vocab ml programming
<!--ID: 1788671819626-->
END

START
English Card
to yield (general)
Back: To **give up control or priority** to something else; to hand over so another party can proceed.
- One core meaning — surrender or give way — used for traffic, arguments, and control flow alike
Russian: уступить, передать управление
Example: At an intersection, you must **yield** to oncoming traffic before turning.
Tags: vocab general english
<!--ID: 1788671819631-->
END

START
English Card
to yield control (async / await context)
Back: To **pause the current task and hand execution back to the event loop** so other tasks can run.
- Python's `await` does exactly this: the coroutine pauses until its result is ready, but the thread is never blocked
Russian: передать управление (событийному циклу)
Example: `await` suspends the current coroutine and **yields** control back to the event loop, letting other coroutines run.
Tags: vocab python async programming
<!--ID: 1788671819635-->
END

START
English Card
to yield (generator / SSE context)
Back: To **produce one value and hand it to the caller**, pausing until the next value is requested.
- In Python, a `yield` inside a function turns it into a generator and freezes its state at that point
- In server-sent events (SSE) each yielded chunk is flushed immediately — the same produce → hand over → pause pattern
Russian: отдать одно значение и приостановиться
Example: The server **yields** each token the moment the LLM produces it — the function pauses after each chunk and resumes when the next one is ready.
Tags: vocab python programming sse generator
<!--ID: 1788671819639-->
END

START
English Card
to flush (networking / I/O context)
Back: To **forcefully empty a buffer and send its contents immediately**, without waiting for more data to accumulate.
- General English is to push something out completely ("flush the pipe"); here it bypasses the normal accumulation wait
Russian: сбросить буфер; отправить немедленно
Example: After each `yield`, FastAPI **flushes** the output buffer — the token travels to the browser right away instead of waiting for more data to pile up.
Tags: vocab networking programming sse io
<!--ID: 1788671819646-->
END

START
English Card
to accumulate
Back: To **gradually collect or build up** over time until a larger amount is reached.
- In networking: bytes or chunks collect in a buffer instead of being sent right away, and flushing empties what has accumulated
Russian: накапливаться; скапливаться
Example: Nginx **accumulates** chunks in its buffer before forwarding — without `X-Accel-Buffering: no`, tokens pile up instead of reaching the browser immediately.
Tags: vocab networking general
<!--ID: 1788671819649-->
END

START
English Card
buffering
Back: **Holding data in memory and delaying its send**, waiting to collect more before transmitting in one batch.
- The opposite of flushing
- General English is to cushion or hold something temporarily ("buffer zone", "buffer time")
Russian: буферизация; накапливание данных перед отправкой
Example: `Content-Type: text/event-stream` tells the browser to activate the SSE parser instead of **buffering** the response as a normal body.
Tags: vocab networking general sse
<!--ID: 1788671820914-->
END

START
English Card
to drill down
Back: To **go deeper into a topic**, moving from a broad overview to specific details.
- In UI/data: navigating from a high-level summary into increasingly granular layers
Russian: углубляться; переходить к деталям
Example: The dashboard shows total revenue — click it and you **drill down** into revenue by country, then by city.
Tags: vocab it ui data
<!--ID: 1788671820920-->
END

START
English Card
to stall
Back: To **halt mid-execution and wait**, unable to continue until something else finishes.
- Literally a vehicle engine stopping from insufficient power
- A stalled thread is alive but making no progress — blocked on I/O, a lock, or a full buffer
Russian: зависнуть; заблокироваться; встать
Example: When the TCP send buffer is full, the server's `write()` call **stalls** — the thread hangs until the client reads some data and frees space.
Tags: vocab networking programming
<!--ID: 1788671820929-->
END

START
English Card
to drain (a buffer)
Back: To **remove data from a buffer by reading it**, freeing space so new data can flow in.
- Literally emptying liquid from a container; the opposite of piling up
Russian: опустошить буфер; вычитать данные из буфера
Example: The client must **drain** the TCP receive buffer fast enough, or the server's send buffer fills up and `write()` blocks.
Tags: vocab networking programming
<!--ID: 1788671820934-->
END

START
English Card
to constrain
Back: To **restrict something within set boundaries** so it cannot go beyond them.
- In tech: limiting a query, scope, or value to an allowed set — a bounded type parameter, a DB `CHECK` constraint
Russian: ограничивать; стеснять рамками
Example: Tight deadlines **constrain** how much we can polish the design before release.
Tags: vocab general it
<!--ID: 1788671820938-->
END

START
English Card
to clobber (IT sense)
Back: To **overwrite existing data destructively**, erasing its previous value.
- From the general "hit hard" sense; one write blindly destroys another, as in the lost update anomaly
- Everyday English sense (to beat decisively) lives in the General deck
Russian: затереть, перезаписать (с потерей данных)
Example: In a lost update, the second writer **clobbers** the first commit with a value computed from stale data.
Tags: vocab concurrency transactions
<!--ID: 1788671820945-->
END

START
English Card
oscillate (ML / signals sense)
Back: To **repeatedly swing above and below a target value** without settling on it.
- Everyday English sense (wavering between opinions) lives in the General deck
Russian: осциллировать, колебаться (вокруг значения)
Example: With too high a learning rate the model **oscillates**, bouncing above and below the correct answer instead of settling.
Tags: vocab verb ml
<!--ID: 1788671820962-->
END

START
English Card
converge (ML / algorithms sense)
Back: To **steadily approach a stable final value**, such as a loss reaching its minimum.
- Everyday English sense (people or ideas coming together) lives in the General deck
Russian: сходиться (к минимуму/решению)
Example: Each overshoot is ~60% of the previous, so training **converges** but wastes iterations.
Tags: vocab verb ml
<!--ID: 1788671820967-->
END

START
English Card
ransom (security sense)
Back: Money demanded by attackers to **restore access to data or systems they have encrypted or seized**.
- The malware that does this is *ransomware*
- Everyday English sense (money for a kidnapped person) lives in the General deck
Russian: выкуп (за данные/доступ)
Example: The malware held the company's data as **ransom**, demanding $1 million to restore access.
Tags: vocab noun security
<!--ID: 1788671820975-->
END

START
English Card
to pile up (networking sense)
Back: To **accumulate in a buffer faster than the receiver consumes it**, until space runs out.
- Everyday English sense (dishes or work piling up) lives in the General deck
Russian: накапливаться (в буфере быстрее, чем обрабатывается)
Example: If the client reads slowly, tokens **pile up** in the TCP send buffer until there is no room left.
Tags: vocab phrasal-verb networking
<!--ID: 1788671820980-->
END

START
English Card
Maven Surefire Plugin
Back: The Maven build plugin that **runs unit tests during the `test` phase**.
- Named from the adjective *surefire* — "sure to fire", so it never misses a test
Russian: плагин Maven для запуска юнит-тестов
Example: If a test throws an unexpected exception, the **Maven Surefire Plugin** marks the build as failed and prints the stack trace.
Tags: vocab noun maven java build-tool
<!--ID: 1788671820985-->
END

START
English Card
OOM — Out of Memory
Back: A fatal error raised when a process has **used up all available memory** and cannot allocate more.
- In Java it surfaces as `java.lang.OutOfMemoryError`, but it is not JVM-specific — the OS, Docker and Kubernetes kill processes for the same reason
Russian: нехватка памяти; ошибка нехватки памяти
Example: The service crashed with an **OOM** error after loading the entire dataset into a list.
Tags: vocab noun abbreviation java
<!--ID: 1788671820991-->
END

START
English Card
to mint (a token)
Back: To **generate and issue a fresh signed token, key, or coin**.
- With asymmetric signing (RS256/ES256) minting requires the **private** key; the public key only verifies, so a client holding it cannot mint an acceptable token
- Everyday English sense (minting coins) lives in the General deck
Russian: выпустить, сгенерировать (токен, ключ)
Example: The auth server **mints** a JWT after login, signing it with its private key.
Tags: vocab verb security jwt crypto
<!--ID: 1788671820997-->
END
