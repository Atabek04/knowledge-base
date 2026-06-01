TARGET DECK: Tech-KB::English Vocab::IT Terms

START
A_English_Translate
To calculate or estimate a missing value by comparing it to similar known values
English: to impute
Russian: Вменять; подставлять (пропущенные значения)
Example: Before training the model, we **imputed** missing ages using the column's median value.
Note: General English: to attribute (blame/credit) to someone. In ML/statistics: to fill in missing data using estimation methods (mean, median, KNN, etc.).
Tags: ml data-preprocessing statistics
<!--ID: 1774613880795-->
END

START
A_English_Translate
A tendency to support or oppose something unfairly, influenced by personal opinions rather than facts
English: bias
Russian: Предубеждение; пристрастие
Example: Hiring decisions can reflect **bias** if interviewers favor candidates from their own background.
Tags: general
<!--ID: 1774613880797-->
END

START
A_English_Translate
A model that learns a distorted version of reality because its training data didn't represent the full picture
English: biased model
Russian: Смещённая модель; модель с предвзятостью
Example: High-income people skipped the income field, so after dropping those rows the **biased model** predicted everyone earns less.
Note: Not the technical bias in y = wx + b. This is the everyday meaning: a systematic blind spot from unrepresentative training data.
Tags: ml data-preprocessing
<!--ID: 1774613880799-->
END

START
A_English_Translate
A data point or observation that is very different from the rest, so it cannot be used to draw general conclusions
English: outlier
Russian: Выброс; аномальное значение
Example: People who live past 100 are genetic **outliers**, whose longevity is unreachable for most of us.
Tags: statistics ml
<!--ID: 1774613880801-->
END

START
A_English_Translate
A column that contains a limited set of distinct labels or groups rather than numbers
English: categorical column
Russian: Категориальный столбец
Example: The "Gender" and "City" columns are **categorical columns** — they hold text labels like "Male" or "London", not numeric values.
Note: Most ML algorithms require converting categorical columns to numbers first (e.g. via one-hot encoding or label encoding).
Tags: ml data-preprocessing
<!--ID: 1774613880802-->
END

START
A_English_Translate
A fixed starting number for a random number generator that ensures the same sequence of "random" results every time
English: seed
Russian: Начальное значение (генератора случайных чисел)
Example: Setting `random_state=42` provides a **seed** so the train-test split is identical every run.
Tags: ml programming
<!--ID: 1774613880804-->
END

START
A_English_Translate
To give up control or priority to something else; to hand over execution flow so another task can proceed.
English: to yield (general)
Russian: уступить, передать управление
Example: At an intersection, you must **yield** to oncoming traffic before turning.
Note: Core meaning: surrender or give way. Used for traffic, arguments, and control flow alike.
Tags: general english
<!--ID: 1780311501633-->
END

START
A_English_Translate
In async programming: to pause the current task and hand execution back to the event loop so other tasks can run.
English: to yield control (async / await context)
Russian: передать управление (событийному циклу)
Example: `await` suspends the current coroutine and **yields** control back to the event loop, letting other coroutines run.
Note: In Python `await` does exactly this — the coroutine is paused at that point until the awaited result is ready, but the thread is not blocked.
Tags: python async programming
<!--ID: 1780311501654-->
END

START
A_English_Translate
To produce one value from a function and hand it to the caller, pausing until the next value is requested.
English: to yield (generator / SSE context)
Russian: отдать одно значение и приостановиться
Example: The server **yields** each token the moment the LLM produces it — the function pauses after each chunk and resumes when the next one is ready.
Note: In Python, `yield` inside a function turns it into a generator. Each `yield` sends one value out and freezes the function's state. In SSE, each yielded chunk is flushed to the client immediately — same "produce one → hand over → pause" pattern.
Tags: python programming sse generator
<!--ID: 1780311501674-->
END

START
A_English_Translate
To forcefully empty a buffer and send its contents immediately, without waiting for more data to accumulate.
English: to flush (networking / I/O context)
Russian: сбросить буфер; отправить немедленно
Example: After each `yield`, FastAPI **flushes** the output buffer — the token travels to the browser right away instead of waiting for more data to pile up.
Note: General English: to flush = push something out completely ("flush the pipe"). In networking/I/O: empty the output buffer and transmit now, bypassing the normal accumulation wait.
Tags: networking programming sse io
<!--ID: 1780311501694-->
END

START
A_English_Translate
To gradually collect or build up over time until a larger amount is reached.
English: to accumulate
Russian: накапливаться; скапливаться
Example: Nginx **accumulates** chunks in its buffer before forwarding — without `X-Accel-Buffering: no`, tokens pile up instead of reaching the browser immediately.
Note: General English: to accumulate = to gather more and more of something over time ("debt accumulates", "snow accumulates"). In networking: bytes or chunks collect in a buffer instead of being sent right away — flushing empties what has accumulated.
Tags: networking general
<!--ID: 1780311501715-->
END

START
A_English_Translate
To temporarily hold data in memory and delay sending it, waiting to collect more before transmitting in one batch.
English: buffering
Russian: буферизация; накапливание данных перед отправкой
Example: `Content-Type: text/event-stream` tells the browser to activate the SSE parser instead of **buffering** the response as a normal body.
Note: General English: to buffer = to cushion or hold something temporarily ("buffer zone", "buffer time"). In networking: the system collects incoming bytes in RAM and holds them until enough have arrived to send efficiently — the opposite of flushing.
Tags: networking general sse
<!--ID: 1780311501736-->
END

START
A_English_Translate
To go deeper into a topic, moving from a broad overview to specific details
English: to drill down
Russian: Углубляться; переходить к деталям
Example: The dashboard shows total revenue — click it and you **drill down** into revenue by country, then by city.
Note: General English: to focus more closely on something. In UI/data: navigating from a high-level summary into increasingly granular layers (dashboard → country → city).
Tags: it ui data
<!--ID: 1780311501757-->
END

START
A_English_Translate
When a running process halts mid-execution and waits, unable to continue until something else finishes
English: to stall
Russian: зависнуть; заблокироваться; встать
Example: When the TCP send buffer is full, the server's `write()` call **stalls** — the thread hangs until the client reads some data and frees space.
Note: Literal: a vehicle engine stalls when it stops due to insufficient power. In computing: a thread/coroutine stalls when it's blocked waiting for I/O, a lock, or a full buffer — it's alive but not making progress.
Tags: networking programming
END

START
A_English_Translate
To remove data from a buffer by reading it, freeing space so new data can flow in
English: to drain (a buffer)
Russian: опустошить буфер; вычитать данные из буфера
Example: The client must **drain** the TCP receive buffer fast enough, or the server's send buffer fills up and `write()` blocks.
Note: Literal: to drain = to empty liquid from a container. In networking: the client "drains" the buffer by reading bytes out — exactly like water flowing out of a sink. The opposite of pile up.
Tags: networking programming
END

START
A_English_Translate
To restrict or limit something within set boundaries so it cannot go beyond them
English: to constrain
Russian: Ограничивать; стеснять рамками
Example: Tight deadlines **constrain** how much we can polish the design before release.
Note: General English: to force someone/something to stay within limits. In tech: limiting a query, scope, or value to an allowed set (e.g. constrain territory to user's allowed unit codes, constrain a type parameter, DB CHECK constraint).
Tags: general it
<!--ID: 1780311501778-->
END
