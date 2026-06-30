type Props = {
    value: string;
    loading: boolean;
    onChange: (val: string) => void;
    onSubmit: () => void;
  };
  
export default function UrlInput({ value, loading, onChange, onSubmit }: Props) {
    return (
      <div className="mb-5">
        <label className="block text-sm font-medium text-slate-700 mb-2">
          长链接地址
        </label>
        <input
          type="url"
          placeholder="https://example.com/very/long/url"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          className="w-full px-4 py-3 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
          onClick={onSubmit}
          disabled={loading}
          className="w-full mt-4 bg-blue-600 hover:bg-blue-700 disabled:bg-blue-300 text-white py-3 rounded-lg font-medium transition"
        >
          {loading ? "生成中..." : "生成短链接"}
        </button>
      </div>
    );
}