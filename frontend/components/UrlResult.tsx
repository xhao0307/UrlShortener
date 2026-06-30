import { copyToClipboard } from "@/utils/clipboard";

type Props = {
  shortUrl: string;
};

export default function UrlResult({ shortUrl }: Props) {
  if (!shortUrl) return null;

  const handleCopy = async () => {
    const success = await copyToClipboard(shortUrl);
    if (success) alert("复制成功！");
  };

  return (
    <div className="mt-6 p-4 bg-green-50 border border-green-200 rounded-lg">
      <p className="text-sm text-green-700 mb-2">✅ 生成成功</p>
      <div className="flex gap-2 items-center break-all">
        <a
          href={shortUrl}
          target="_blank"
          rel="noopener noreferrer"
          className="text-blue-600 flex-1"
        >
          {shortUrl}
        </a>
        <button
          onClick={handleCopy}
          className="shrink-0 px-3 py-1 bg-green-600 text-white rounded text-sm"
        >
          复制
        </button>
      </div>
    </div>
  );
}