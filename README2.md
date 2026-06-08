# Logic behind: range(1, NMAX + 1)

Start at **1**

Stop at **NMAX**

Go up by **1 each time**

But here’s the key…

In Python, `range(start, stop)` **does NOT include the stop value** .

So if you did:

<pre class="overflow-visible! px-0!" data-start="238" data-end="263"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>range</span><span>(</span><span>1</span><span>, </span><span>5</span><span>)
</span></span></code></div></div></pre>

You get:

<pre class="overflow-visible! px-0!" data-start="274" data-end="292"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>1, 2, 3, 4
</span></span></code></div></div></pre>

Not 5.

So when someone writes:

<pre class="overflow-visible! px-0!" data-start="326" data-end="358"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>range</span><span>(</span><span>1</span><span>, NMAX + </span><span>1</span><span>)
</span></span></code></div></div></pre>

They’re forcing Python to include `NMAX`.

Example:

<pre class="overflow-visible! px-0!" data-start="413" data-end="478"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-python"><span><span>NMAX = </span><span>10</span><span>
</span><span>for</span><span> i </span><span>in</span><span></span><span>range</span><span>(</span><span>1</span><span>, NMAX + </span><span>1</span><span>):
    </span><span>print</span><span>(i)
</span></span></code></div></div></pre>

This prints:

<pre class="overflow-visible! px-0!" data-start="493" data-end="521"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>1 2 3 4 5 6 7 8 9 10
</span></span></code></div></div></pre>

If you removed the `+ 1`:

You’d only go to 9.

So the logic is:

Python stops right before the second number

So we add 1 to reach the real max.

# FOR LOOPS, range(), AND len() CHEAT SHEET

## 1. Use Neither When You Only Need the Values

```python
friends = ["Harry", "Emily", "Bob"]

for friend in friends:
    print(friend)
```

Output:

```python
Harry
Emily
Bob
```

Use this when you only care about the values.

Memory Trick:

```python
for item in myList:
```

✅ Need VALUES

---

## 2. Use len() When You Need the Count

```python
friends = ["Harry", "Emily", "Bob"]

print("Number of friends:", len(friends))
```

Output:

```python
Number of friends: 3
```

Use this when you need to know how many elements are in a list.

Memory Trick:

```python
len(myList)
```

✅ Need COUNT

---

## 3. Use range(len()) When You Need the Indexes

```python
friends = ["Harry", "Emily", "Bob"]

for i in range(len(friends)):
    print("Index:", i, "Value:", friends[i])
```

Output:

```python
Index: 0 Value: Harry
Index: 1 Value: Emily
Index: 2 Value: Bob
```

Use this when you need the index positions.

Memory Trick:

```python
for i in range(len(myList)):
```

✅ Need INDEXES

---

## Why range() Is Important

This does NOT work:

```python
friends = ["Harry", "Emily", "Bob"]

for i in friends:
    print(friends[i])
```

Problem:

```python
i = "Harry"
```

Python tries:

```python
friends["Harry"]
```

Crash ❌

Because list indexes must be numbers.

---

This DOES work:

```python
friends = ["Harry", "Emily", "Bob"]

for i in range(len(friends)):
    print(friends[i])
```

Python creates:

```python
i = 0
i = 1
i = 2
```

Which becomes:

```python
friends[0]
friends[1]
friends[2]
```

Valid ✅

---

## What range(len(friends)) Actually Does

```python
friends = ["Harry", "Emily", "Bob"]

print(len(friends))
```

Output:

```python
3
```

Then:

```python
range(3)
```

Produces:

```python
0
1
2
```

So:

```python
for i in range(len(friends)):
```

Really means:

```python
for i in [0, 1, 2]:
```

---

## Quick Reference

```python
for item in myList:
```

✅ Need VALUES

```python
len(myList)
```

✅ Need COUNT

```python
for i in range(len(myList)):
```

✅ Need INDEXES

---

## Ultimate Memory Trick

```python
for item in myList
```

"Give me the VALUES."

```python
len(myList)
```

"Tell me how many."

```python
range(len(myList))
```

"Give me every index."
