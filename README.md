<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PyLeitner CLI - Documentation</title>
    <style>
        :root {
            --primary-color: #0366d6;
            --text-color: #24292e;
            --bg-color: #ffffff;
            --code-bg: #f6f8fa;
            --code-block-bg: #2d333b;
            --code-block-text: #adbac7;
            --border-color: #e1e4e8;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            background-color: var(--bg-color);
        }

        h1, h2, h3 {
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }

        h1 {
            font-size: 2.5em;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.3em;
        }

        h2 {
            font-size: 1.75em;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.3em;
            margin-top: 50px;
        }

        h3 {
            font-size: 1.25em;
        }

        p {
            margin-bottom: 16px;
        }

        a {
            color: var(--primary-color);
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        ul {
            padding-left: 2em;
            margin-bottom: 16px;
        }

        li {
            margin-bottom: 8px;
        }

        code {
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
            font-size: 85%;
            background-color: var(--code-bg);
            padding: 0.2em 0.4em;
            border-radius: 3px;
        }

        pre {
            background-color: var(--code-block-bg);
            color: var(--code-block-text);
            padding: 16px;
            overflow: auto;
            border-radius: 6px;
            margin-bottom: 16px;
        }

        pre code {
            background-color: transparent;
            padding: 0;
            font-size: 100%;
            color: inherit;
        }

        .badges {
            margin-bottom: 20px;
        }

        .badges img {
            margin-right: 5px;
        }

        blockquote {
            margin: 0;
            padding: 0 1em;
            color: #6a737d;
            border-left: 0.25em solid #dfe2e5;
        }

        table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 16px;
        }

        th, td {
            padding: 6px 13px;
            border: 1px solid var(--border-color);
        }

        th {
            background-color: var(--code-bg);
            font-weight: 600;
        }
        
        /* Syntax highlighting simulation */
        .comment { color: #8b949e; font-style: italic; }
        .keyword { color: #ff7b72; }
        .string { color: #a5d6ff; }
        .number { color: #79c0ff; }
    </style>
</head>
<body>

    <header>
        <h1>🧠 PyLeitner CLI</h1>
        <h3>High-Performance Spaced Repetition System</h3>
        
        <div class="badges">
            <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python" alt="Python">
            <img src="https://img.shields.io/badge/PostgreSQL-14%2B-336791?style=flat-square&logo=postgresql" alt="PostgreSQL">
            <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License">
        </div>

        <p><strong>PyLeitner CLI</strong> is a robust, terminal-based implementation of the Leitner System, designed for efficient memory retention through algorithmic spaced repetition. Built with Python and PostgreSQL, it features persistent storage, user authentication, and an automated penalty system for overdue cards.</p>
    </header>

    <nav>
        <h2>📑 Table of Contents</h2>
        <ul>
            <li><a href="#architecture">Architecture & Features</a></li>
            <li><a href="#logic">Algorithmic Logic</a></li>
            <li><a href="#installation">Installation</a></li>
            <li><a href="#configuration">Configuration</a></li>
            <li><a href="#usage">Usage</a></li>
            <li><a href="#structure">Project Structure</a></li>
        </ul>
    </nav>

    <section id="architecture">
        <h2>🏗 Architecture & Features</h2>
        <p>The application is structured as a modular CLI tool interacting with a relational database backend.</p>
        <ul>
            <li><strong>Persistent Storage:</strong> Utilizes <code>psycopg2</code> for robust interaction with a PostgreSQL database.</li>
            <li><strong>User Authentication:</strong> Secure registration and login flows with regex-based input validation.</li>
            <li><strong>Automated Schema Management:</strong> Self-healing database setup; automatically detects and initializes the database and tables (<code>users</code>, <code>cards</code>) upon first launch.</li>
            <li><strong>Multi-Slot Leitner System:</strong> Supports a 6-slot learning pipeline.</li>
            <li><strong>Graceful Error Handling:</strong> Comprehensive <code>try-except</code> blocks for database transactions and user I/O.</li>
        </ul>
    </section>

    <section id="logic">
        <h2>🧮 Algorithmic Logic</h2>
        
        <h3>1. Spaced Repetition Review</h3>
        <p>The core review mechanism retrieves cards from specific slots.</p>
        <ul>
            <li><strong>Success (y):</strong> The card is promoted to <code>Current Slot + 1</code>.</li>
            <li><strong>Failure (n):</strong> The card remains in the <code>Current Slot</code> (Retention Strategy).</li>
        </ul>

        <h3>2. The Penalty Policy (<code>apply_penalty_policy</code>)</h3>
        <p>To ensure consistency, the system runs a background check before every review session:</p>
        <ul>
            <li><strong>Calculation:</strong> <code>Deadline = Last Review Date + Slot Interval + 2 Days (Grace Period)</code></li>
            <li><strong>Penalty:</strong> If the current date exceeds the Deadline, the card is demoted: <code>New Slot = max(1, Current Slot - 1)</code>.</li>
        </ul>
    </section>

    <section id="installation">
        <h2>⚡ Installation</h2>
        
        <h3>Prerequisites</h3>
        <ul>
            <li>Python 3.8+</li>
            <li>PostgreSQL Server</li>
        </ul>

        <h3>Steps</h3>
        <p>1. <strong>Clone the Repository</strong></p>
        <pre><code>git clone https://github.com/yourusername/pyleitner-cli.git
cd pyleitner-cli</code></pre>

        <p>2. <strong>Set up Virtual Environment (Recommended)</strong></p>
        <pre><code>python -m venv venv
source venv/bin/activate  <span class="comment"># On Windows: venv\Scripts\activate</span></code></pre>

        <p>3. <strong>Install Dependencies</strong></p>
        <pre><code>pip install psycopg2-binary</code></pre>
    </section>

    <section id="configuration">
        <h2>⚙️ Configuration</h2>
        <p>The application requires a <code>config.py</code> file in the root directory to handle database credentials and Leitner intervals.</p>
        <p>1. Create a file named <code>config.py</code>.</p>
        <p>2. Paste the following configuration:</p>

<pre><code><span class="comment"># config.py</span>

<span class="comment"># Database Credentials</span>
DB_NAME = <span class="string">"leitner_db"</span>
DB_USER = <span class="string">"postgres"</span>
DB_PASS = <span class="string">"your_password"</span>
DB_HOST = <span class="string">"localhost"</span>
DB_PORT = <span class="string">"5432"</span>

<span class="comment"># Leitner System Intervals (Slot: Days)</span>
<span class="comment"># Defines how often cards in each slot should be reviewed</span>
BOX_INTERVALS = {
    <span class="number">1</span>: <span class="number">1</span>,   <span class="comment"># Review every day</span>
    <span class="number">2</span>: <span class="number">2</span>,   <span class="comment"># Review every 2 days</span>
    <span class="number">3</span>: <span class="number">4</span>,   <span class="comment"># Review every 4 days</span>
    <span class="number">4</span>: <span class="number">8</span>,   <span class="comment"># Review every 8 days</span>
    <span class="number">5</span>: <span class="number">16</span>,  <span class="comment"># Review every 16 days</span>
    <span class="number">6</span>: <span class="number">30</span>   <span class="comment"># Review every month</span>
}</code></pre>
    </section>

    <section id="usage">
        <h2>🚀 Usage</h2>
        <p>Run the entry point script to start the application:</p>
        <pre><code>python main.py</code></pre>

        <h3>Workflow</h3>
        <ol>
            <li><strong>Register/Login:</strong> Create an account. Your data is isolated from other users by <code>user_id</code>.</li>
            <li><strong>Add Cards:</strong> Enter data in <code>Question :: Answer</code> format.</li>
            <li><strong>Review:</strong> Select a slot. The system automatically calculates penalties before showing cards.</li>
            <li><strong>Modify:</strong> Edit or delete cards directly from specific slots.</li>
        </ol>
    </section>

    <section id="structure">
        <h2>📂 Project Structure</h2>
<pre><code>.
├── main.py         <span class="comment"># Entry point & Menu orchestration</span>
├── auth.py         <span class="comment"># Authentication logic (Register/Login)</span>
├── cards.py        <span class="comment"># CRUD operations for Flashcards</span>
├── review.py       <span class="comment"># Leitner algorithm & Penalty logic</span>
├── db.py           <span class="comment"># Database connection & Schema initialization</span>
├── utils.py        <span class="comment"># Helper functions (Clear screen, I/O)</span>
├── config.py       <span class="comment"># Configuration variables (Not included in repo)</span>
└── README.md       <span class="comment"># Documentation</span></code></pre>
    </section>

    <section id="contributing">
        <h2>🤝 Contributing</h2>
        <p>Contributions are welcome! Please ensure any Pull Requests targeting the core logic include unit tests for the <code>apply_penalty_policy</code> function.</p>
        <ol>
            <li>Fork the Project</li>
            <li>Create your Feature Branch (<code>git checkout -b feature/AmazingFeature</code>)</li>
            <li>Commit your Changes (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
            <li>Push to the Branch (<code>git push origin feature/AmazingFeature</code>)</li>
            <li>Open a Pull Request</li>
        </ol>
    </section>

    <footer style="margin-top: 50px; padding-top: 20px; border-top: 1px solid #eaecef; text-align: center; color: #666;">
        <p>Generated for PyLeitner CLI Project</p>
    </footer>

</body>
</html>
