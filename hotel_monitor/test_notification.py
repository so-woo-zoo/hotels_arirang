#!/usr/bin/env python3
"""
通知サンプル送信スクリプト
実際の通知がどんな見た目になるか確認するためのテスト用。
本番コードとは独立しており、監視には影響しない。
"""

import os
import requests

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "")


def post_discord(payload: dict) -> None:
    if not DISCORD_WEBHOOK_URL:
        print("[Discord] DISCORD_WEBHOOK_URL が未設定です")
        return
    resp = requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=10)
    if resp.status_code == 204:
        print("✅ 送信成功！")
    else:
        print(f"❌ 送信失敗: HTTP {resp.status_code} / {resp.text}")


def main():
    booking_url = (
        "https://be4.wingsbooking.com/KTREE1111/roomSelect"
        "?check_in=2027-06-10&check_out=2027-06-11"
        "&rooms=1&adult=1&children=0&channel_code=WINGS_B2C"
    )

    # --- 新着通知のサンプル ---
    new_payload = {
        "content": (
            "🆕 **新着の空室**（2件）｜ ☁️ GitHub Actions\n"
            "\n"
            "📅 **2027-06-10**\n"
            "🏙 **高陽**\n"
            f"・[K-Tree Hotel スタンダードダブル]({booking_url}) ₩130,000（≈¥14,300）\n"
            f"・[K-Tree Hotel デラックスダブル]({booking_url}) ₩160,000（≈¥17,600）\n"
            "\n"
            "📅 **2027-06-11**\n"
            "🏙 **高陽**\n"
            f"・[K-Tree Hotel スタンダードダブル]({booking_url}) ₩130,000（≈¥14,300）\n"
        ),
        "flags": 4,
    }
    print("【新着通知】送信中...")
    post_discord(new_payload)

    import time
    time.sleep(1)

    # --- 継続通知のサンプル ---
    old_payload = {
        "content": (
            "📋 **継続中の空室**（1件）｜ ☁️ GitHub Actions\n"
            "\n"
            "📅 **2027-06-12**\n"
            "🏙 **高陽**\n"
            f"・[K-Tree Hotel スタンダードダブル]({booking_url}) ₩130,000（≈¥14,300）\n"
        ),
        "flags": 4,
    }
    print("【継続通知】送信中...")
    post_discord(old_payload)


if __name__ == "__main__":
    main()
