class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        st = set()
        for address in emails:
            localName, domainName = address.split('@')
            if (idx := localName.find('+'))!= -1:
                localName = localName[:idx]
            st.add(localName.replace('.','') + '@' + domainName)
        print(st)
        return len(st)