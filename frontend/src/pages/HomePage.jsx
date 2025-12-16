import Summary from "../components/Summary"
import TransactionTable from "../components/TransactionTable"
import AddTransaction from "../components/AddTransaction"
import { useState, useEffect } from "react"

export default function HomePage() {
    // Prepare state
    const [budget, setBudget] = useState()

    // Load summary sectoin on initial render and remountings

    // Load transactions table on initial render and subsequent remountings


    return(
        <div className="home-page">
            <h2>Welcome to Pocket Plan. App is under construction.</h2>
            <Summary/>
            <AddTransaction/>
            <TransactionTable/>
        </div>
    )
}