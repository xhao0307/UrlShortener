type Props = {
    msg: string;
  };

export default function ErrorTip({ msg }: Props) {
    if (!msg) return null;
    return <p className="mt-4 text-red-500 text-center">{msg}</p>;
}
