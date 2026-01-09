def fizzbuzz(n):
    """
    FizzBuzzの結果を返す関数

    Args:
        n (int): 処理する数値

    Returns:
        str or int: FizzBuzz処理の結果

    Raises:
        TypeError: nが整数でない場合、またはbool型の場合
        ValueError: nが正の整数でない場合
        OverflowError: nが大きすぎる場合
    """
    # bool型のチェック（Pythonではboolはintのサブクラスだが、除外する）
    if isinstance(n, bool):
        raise TypeError(f"引数は整数である必要があります: bool型が渡されました")

    if not isinstance(n, int):
        raise TypeError(
            f"引数は整数である必要があります: {type(n).__name__}が渡されました"
        )

    if n <= 0:
        raise ValueError(f"引数は正の整数である必要があります: {n}が渡されました")

    # 非常に大きな数値のチェック（実用性を考慮）
    if n > 10**9:
        raise OverflowError(f"引数が大きすぎます: {n} (最大値: 10^9)")

    out = ""
    if n % 3 == 0:
        out += "Fizz"
    if n % 5 == 0:
        out += "Buzz"
    return out or n


def fizzbuzz_range(start, end):
    """
    指定範囲のFizzBuzzを実行

    Args:
        start (int): 開始値
        end (int): 終了値（この値を含む）

    Returns:
        list: FizzBuzz結果のリスト

    Raises:
        TypeError: start または end が整数でない場合、またはbool型の場合
        ValueError: start または end が正の整数でない場合、または start > end の場合
        OverflowError: 範囲が大きすぎる場合
    """
    # bool型のチェック
    if isinstance(start, bool) or isinstance(end, bool):
        raise TypeError("start と end は整数である必要があります（bool型は不可）")

    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start と end は整数である必要があります")

    if start <= 0 or end <= 0:
        raise ValueError("start と end は正の整数である必要があります")

    if start > end:
        raise ValueError(f"start ({start}) は end ({end}) より小さい必要があります")

    # 範囲が大きすぎる場合のチェック
    if (end - start + 1) > 10**6:
        raise OverflowError(
            f"範囲が大きすぎます: {end - start + 1} 個の要素（最大: 10^6）"
        )

    results = []
    for i in range(start, end + 1):
        results.append(fizzbuzz(i))
    return results


if __name__ == "__main__":
    # FizzBuzz: 1～20 を出力
    try:
        results = fizzbuzz_range(1, 20)
        for result in results:
            print(result)
    except (TypeError, ValueError) as e:
        print(f"エラー: {e}")
