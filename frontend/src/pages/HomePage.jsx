import Budget from "../components/Budget"
import TransactionTable from "../components/TransactionTable"
import AddTransaction from "../components/AddTransaction"

export default function HomePage() {
    return(
        <div className="home-page">
            <h2>Welcome to Pocket Plan. App is under construction.</h2>
            <Budget/>
            <AddTransaction/>
            <TransactionTable/>
        </div>
    )
}