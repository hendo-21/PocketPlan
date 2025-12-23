import { MdOutlineEditNote } from "react-icons/md";

export default function TransactionTableRow({ transaction }) {
    return (
        <tr>
            <td>{transaction.date}</td>
            <td>${transaction.amount}</td>
            <td>{transaction.memo}</td>
            <td><MdOutlineEditNote/></td>
        </tr>
    )
}