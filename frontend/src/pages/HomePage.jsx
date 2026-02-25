// Components
import Summary from "../components/Summary"
import TransactionTable from "../components/TransactionTable"
import AddTransaction from "../components/AddTransaction"

// React functions
import { useState, useEffect } from "react";

// Icons
import { AiFillRedEnvelope } from "react-icons/ai";

export default function HomePage() {
    // Prepare state for loading data
    const [summaries, setSummary] = useState([]);
    const [transactions, setTransactions] = useState([]);
    const [totalSpent, setTotalSpent] = useState(0.0);

    // Prepare state to render edit and add forms
    const [isEditing, setIsEditing] = useState('');
    const [isAdding, setIsAdding] = useState(false);
    const [isEditingSummary, setIsEditingSummary] = useState(false);


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
        loadSummary();
        loadTransactions();
        loadTotalSpent();
    }, [])

    // Edit summary - load the summary component
    const onSummaryEdit = async (id, budget) => {
        const new_budget = { budget };
        const edited_summary_res = await fetch(`/api/summaries/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(new_budget)
        })
        if(edited_summary_res.status === 200) {
            loadSummary();
            loadTotalSpent();
            loadTransactions();
        } else {
            console.log(`Failed to update summary. Status code: ${edited_summary_res.status}`);
        }
    }

    // Delete transaction - call REST API
    const onDelete = async (id) => {
        const delete_res = await fetch(
            `/api/transactions/${id}`,
            { method: 'DELETE'}
        );
        if(delete_res.status === 204) {
            loadTotalSpent;
            loadSummary();
            loadTotalSpent();
            loadTransactions();
        }
        else {
            console.log(`Failed to delete transaction with ID ${id}. Status code: ${delete_res.status}`);
        }
    }

    // Edit transaction
    const onEdit = async (id, date_added, amount, memo) => {
        const edited_transaction = { date_added, amount, memo };
        const edited_tr_res = await fetch(`/api/transactions/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(edited_transaction)
        });
        if(edited_tr_res.status === 200) {
            loadSummary();
            loadTotalSpent();
            loadTransactions();
        } else {
            console.log(`Failed to update transaction with ID ${id}. Status code: ${edited_tr_res.status}`);
        }
    }

    // Return the HTML
    return(
        <div className="home-page">

            <div className="app-header">
                <AiFillRedEnvelope />
                <h4>Fun spend</h4>
            </div>

            <Summary 
                summary={summaries[0]} 
                totalSpent={totalSpent} 
                isEditingSummary={isEditingSummary} 
                setIsEditingSummary={setIsEditingSummary} 
                onSummaryEdit={onSummaryEdit}
            />

            <div className="add-transaction-container">
                {isAdding ? (
                    <AddTransaction setIsAdding={setIsAdding} loadTotalSpent={loadTotalSpent} loadTransactions={loadTransactions}/> )
                    : (
                    <button onClick={() => setIsAdding(true)}>Add Transaction</button>
                    )}
            </div>

            <TransactionTable 
                transactions={transactions} 
                isEditing={isEditing} 
                setIsEditing={setIsEditing}
                onEdit={onEdit}
                onDelete={onDelete} 
            />

        </div>
    )
}