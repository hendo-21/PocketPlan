// Components
import Summary from "../components/Summary"
import TransactionTable from "../components/TransactionTable"
import AddTransaction from "../components/AddTransaction"

// React functions
import { useState, useEffect } from "react"

// Icons
import { AiFillRedEnvelope } from "react-icons/ai";

export default function HomePage() {
    // Prepare state
    const [summaries, setSummary] = useState([])
    const [transactions, setTransactions] = useState([])
    const [isAdding, setIsAdding] = useState(false)
    const [totalSpent, setTotalSpent] = useState(0.0)


    // Fetch summary data from db
    const loadSummary = async () => {
        const response = await fetch('/api/summaries');
        const summaryData = await response.json();
        setSummary(summaryData);
    }

    // Fetch total spent for Summary component
    const loadTotalSpent = async () => {
        const response = await fetch('/api/transactions/total-spend');
        const totalSpent = await response.json();
        console.log('New total', totalSpent);
        setTotalSpent(totalSpent);
    }

    // Fetch transaction data from db
    const loadTransactions = async () => {
        const response = await fetch('/api/transactions');
        const transactionsData = await response.json();
        setTransactions(transactionsData);
    }

    // Load summary, transaction data, and total spent on initial render and re-mountings
    useEffect(() => {
        loadSummary()
        loadTransactions()
        loadTotalSpent()
    }, [])

    // Delete summary - call REST API
    const onDelete = async (id) => {
        const delete_res = await fetch(
            `/api/transactions/${id}`,
            { method: 'DELETE'}
        );
        if(delete_res.status === 204) {
            loadSummary();
            loadTotalSpent();
            loadTransactions();
        }
        else {
            console.log(`Failed to delete transaction with ID ${id}. Status code: ${delete_res.status}`);
        }
    }

    // Edit summary - load the summary component (form with pre-loaded values)

    // Edit transaction - load the summary component (form with pre-loaded values)

    // Return the HTML
    return(
        <div className="home-page">
            <div className="app-header">
                <AiFillRedEnvelope />
                <h4>Fun spend</h4>
            </div>
            <Summary summary={summaries[0]} totalSpent={totalSpent}/>
            <div className="add-transaction-container">
                {isAdding ? (
                    <AddTransaction setIsAdding={setIsAdding} loadTotalSpent={loadTotalSpent} loadTransactions={loadTransactions}/> )
                    : (
                    <button onClick={() => setIsAdding(true)}>Add Transaction</button>
                    )}
            </div>
            <TransactionTable transactions={transactions} onDelete={onDelete}/>
        </div>
    )
}