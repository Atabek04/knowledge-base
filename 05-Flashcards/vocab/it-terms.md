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
END

START
A_English_Translate
In async programming: to pause the current task and hand execution back to the event loop so other tasks can run.
English: to yield control (async / await context)
Russian: передать управление (событийному циклу)
Example: `await` suspends the current coroutine and **yields** control back to the event loop, letting other coroutines run.
Note: In Python `await` does exactly this — the coroutine is paused at that point until the awaited result is ready, but the thread is not blocked.
Tags: python async programming
END
