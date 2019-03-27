class Solution:

    def handle(self, email: str):
        two = email.split('@')
        fore = two[0]
        post = two[1]
        fore = fore.replace('.', '')
        fore = fore.split('+')[0]
        return '{}@{}'.format(fore, post)

    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()

        for x in emails:
            after = self.handle(x)
            result.add(after)

        return len(result)