import Summary from "../components/Summary"
import TransactionTable from "../components/TransactionTable"
import AddTransaction from "../components/AddTransaction"
import { useState, useEffect } from "react"

export default function HomePage() {
    // Prepare state
    const [summaries, setSummary] = useState([])
    const [transactions, setTransactions] = useState([])

    // Fetch summary data from db
    const loadSummary = async () => {
        const response = await fetch('/api/summaries');
        const summaryData = await response.json();
        setSummary(summaryData);
    }

    // Fetch transaction data from db
    const loadTransactions = async () => {
        const response = await fetch('/api/transactions');
        const transactionsData = await response.json();
        setTransactions(transactionsData);
    }

    // Load summary and transaction data on initial render and re-mountings
    useEffect(() => {
        loadSummary()
        loadTransactions()
    }, [])

    // Delete summary - call REST API

    // Edit summary - load the summary component (form with pre-loaded values)

    // Delete transaction- call REST API

    // Edit transaction - load the summary component (form with pre-loaded values)


    return(
        <div className="home-page">
            <h2>Welcome to Pocket Plan. App is under construction.</h2>
            <Summary summary={summaries[0]}/>
            <AddTransaction/>
            <TransactionTable transactions={transactions}/>
        </div>
    )
}