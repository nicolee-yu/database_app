from sec_api import ExtractorApi, QueryApi

API_KEY = "3a8cca5da1e545b033746eeb287cf7c6ddc5fd6500354e3aa1441d3e8ab9dda7"
extractorApi = ExtractorApi(API_KEY)
queryApi = QueryApi(API_KEY)


def extract_item_1a_text(filing_url: str) -> str:
    try:
        return extractorApi.get_section(filing_url, '1A', 'text')
    except Exception as e:
        return f"❌ Error extracting Item 1A: {str(e)}"


def find_10k_filing_url(company: str, year: str) -> str:
    """
    查找指定公司和年份的 10-K filing 的链接
    """
    query = {
        "query": f"ticker:{company.upper()} AND formType:\"10-K\"",
        "from": "0",
        "size": "10",
        "sort": [{"filedAt": {"order": "desc"}}]
    }

    results = queryApi.get_filings(query)
    for filing in results.get("filings", []):
        if year in filing["filedAt"]:
            return filing["linkToHtml"]

    return "❌ No 10-K filing found for this year."
