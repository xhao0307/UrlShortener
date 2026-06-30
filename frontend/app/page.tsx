"use client";

import { useState } from "react";
import { createShortUrl } from "@/api/urlApi";
import UrlInput from "@/components/UrlInput";
import UrlResult from "@/components/UrlResult";
import ErrorTip from "@/components/ErrorTip";

export default function Home() {
  const [originalUrl, setOriginalUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  const handleGenerate = async () => {
    setErrorMsg("");
    setShortUrl("");

    if (!originalUrl.trim()) {
      setErrorMsg("请输入需要缩短的完整链接");
      return;
    }

    try {
      setLoading(true);
      const data = await createShortUrl(originalUrl);
      setShortUrl(data.short_url);
    } catch (err: any) {
      if (err.response?.data?.detail) {
        setErrorMsg(err.response.data.detail);
      } else {
        setErrorMsg("请求失败，请确认后端服务已启动在8000端口");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-slate-100 flex items-center justify-center p-4">
      <div className="w-full max-w-lg bg-white rounded-xl shadow-lg p-8">
        <h1 className="text-3xl font-bold text-center text-slate-800 mb-8">
          URL 短链接生成器
        </h1>

        <UrlInput
          value={originalUrl}
          loading={loading}
          onChange={setOriginalUrl}
          onSubmit={handleGenerate}
        />

        <ErrorTip msg={errorMsg} />

        <UrlResult shortUrl={shortUrl} />
      </div>
    </main>
  );
}