class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        record = dict()

        for domains in cpdomains:
            times = int(domains.split(' ')[0])
            url = domains.split(' ')[1]

            parts = url.split('.')

            length = len(parts)
            for x in range(length):
                sub = parts[x:]
                suburl = ''

                for y in sub:
                    suburl += y + '.'

                suburl = suburl[:-1]

                t = record.get(suburl)
                if t is None:
                    record[suburl] = times
                else:
                    record[suburl] += times

        result = []

        for x in record.keys():
            string = str(record.get(x)) + ' ' + x
            result.append(string)

        return result