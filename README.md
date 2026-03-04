# Fun Money Tracker

## GIF
[Demo](demo.gif)

## Description
A simple full stack personal finance web app for tracking discretionary spending.

## Context
My partner and I have had combined finances for a couple of years now. We employ a budgeting strategy that's similar to the cash stuffing strategy: our income goes into one pot, and we pay for our bills and necessities from that pot. We also pay ourselves discretionary money. In an increasingly cashless world, tracking these "fun money" transactions, as we call them, became a pain. 

Banking and budgeting apps provide way more features than we needed. This simple web app has all of what we need and none of what we don't.

## Tech Stack
- Frontend: React, Vite, CSS
- Backend: Python, Flask, SQLAlchemy
- Database: SQLite
- Deployment: Fly.io, Docker
    - Deployed twice: once for myself, once for my partner

## Features
- Add, edit and delete transactions from a ledger.
- Live-updating summary including editable budget.
- Persistent data storage.

## Project Structure
```
.
├── backend - REST API and database model definitions. Flask & SQLAlchemy
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
│   └── test-requests.http
├── frontend - SPA components and UI. React/Vite
│   ├── src
│   │   ├── assets
│   │   ├── components
│   │   ├── pages
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   ├── eslint.config.js
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   └── vite.config.js
├── Dockerfile
├── fly-ian.toml
├── output.txt
└── README.md
```

## What I Learned
I was motivated by a desire to move beyond my coursework stack, and I wanted a solution that was super light weight, knowing the target customers were myself and my wife. My goals with this project were to:
- Experience a new tech stack that used relational databases via an ORM
    - Ultimately this was unnecessary given the simplicity of the database design
- Build a REST API using Python
- Develop my frontend skills with React
- Host the web app so that it can actually be used

## Future Improvements
UI:
- Bulk delete for transactions
- Display previous summaries
- Carry over under/over spending into next month

User authentication. Currently have one deployed for myself and one for my partner.

## License
[MIT](LICENSE)
