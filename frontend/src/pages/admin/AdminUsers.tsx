import React, { useState, useEffect } from 'react';
import { api } from '../../services/api';
import { Users, Shield, Check, X, Search, UserCheck, UserX } from 'lucide-react';

export const AdminUsers: React.FC = () => {
  const [users, setUsers] = useState<any[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [search, setSearch] = useState<string>('');

  const loadUsers = async () => {
    try {
      const data = await api.getAdminUsers();
      setUsers(data);
    } catch (err) {
      console.error('Failed to load users:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadUsers();
  }, []);

  const handleToggle = async (userId: number) => {
    try {
      await api.toggleUserStatus(userId);
      setUsers((prev) =>
        prev.map((u) => (u.id === userId ? { ...u, is_active: !u.is_active } : u))
      );
    } catch (err: any) {
      alert(err.message || 'Cannot toggle user status');
    }
  };

  const filtered = users.filter(
    (u) =>
      u.full_name.toLowerCase().includes(search.toLowerCase()) ||
      u.email.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="space-y-6 max-w-6xl mx-auto pb-12">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-surface-border pb-5">
        <div>
          <span className="text-xs font-bold uppercase tracking-wider text-brand-600">Directory</span>
          <h1 className="text-2xl font-bold text-navy-800 mt-1">User & Role Management</h1>
        </div>

        <div className="relative w-full sm:w-80">
          <Search className="absolute left-3.5 top-3 h-4 w-4 text-slateText-muted" />
          <input
            type="text"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search by name or email..."
            className="w-full rounded-xl border border-slate-300 bg-white pl-10 pr-4 py-2.5 text-xs text-slateText-primary focus:outline-none focus:border-brand-600 focus:ring-2 focus:ring-brand-500/20 transition-all shadow-xs"
          />
        </div>
      </div>

      {loading ? (
        <div className="flex h-64 items-center justify-center">
          <div className="h-8 w-8 animate-spin rounded-full border-4 border-brand-600 border-t-transparent" />
        </div>
      ) : (
        <div className="rounded-2xl border border-surface-border bg-white overflow-hidden shadow-card">
          <table className="w-full text-left text-xs text-slateText-primary">
            <thead className="bg-slate-50 border-b border-surface-border text-[11px] uppercase tracking-wider text-slateText-secondary">
              <tr>
                <th className="px-6 py-4 font-extrabold">Name & Email</th>
                <th className="px-6 py-4 font-extrabold">Role</th>
                <th className="px-6 py-4 font-extrabold">Account Status</th>
                <th className="px-6 py-4 font-extrabold">Registration Date</th>
                <th className="px-6 py-4 font-extrabold text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {filtered.map((u) => (
                <tr key={u.id} className="hover:bg-brand-50/30 transition-colors">
                  <td className="px-6 py-4.5">
                    <div className="font-bold text-navy-800 text-sm">{u.full_name}</div>
                    <div className="text-[11px] text-slateText-muted font-mono mt-0.5">{u.email}</div>
                  </td>
                  <td className="px-6 py-4.5">
                    <span
                      className={`px-3 py-1 rounded-full text-[10px] font-extrabold uppercase border ${
                        u.role === 'admin'
                          ? 'bg-purple-50 text-purple-700 border-purple-200'
                          : 'bg-brand-50 text-brand-700 border-brand-200'
                      }`}
                    >
                      {u.role}
                    </span>
                  </td>
                  <td className="px-6 py-4.5">
                    <span
                      className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-[11px] font-bold border ${
                        u.is_active
                          ? 'bg-emerald-50 text-emerald-700 border-emerald-200'
                          : 'bg-rose-50 text-rose-700 border-rose-200'
                      }`}
                    >
                      <span
                        className={`h-2 w-2 rounded-full ${
                          u.is_active ? 'bg-emerald-500 animate-pulse' : 'bg-rose-500'
                        }`}
                      />
                      {u.is_active ? 'Active' : 'Suspended'}
                    </span>
                  </td>
                  <td className="px-6 py-4.5 text-slateText-secondary font-medium">
                    {new Date(u.created_at).toLocaleDateString('en-US', {
                      year: 'numeric',
                      month: 'short',
                      day: 'numeric',
                    })}
                  </td>
                  <td className="px-6 py-4.5 text-right">
                    <button
                      onClick={() => handleToggle(u.id)}
                      className={`inline-flex items-center gap-1.5 rounded-xl px-3.5 py-1.5 text-xs font-bold border transition-all cursor-pointer active:scale-95 shadow-2xs ${
                        u.is_active
                          ? 'border-rose-200 text-rose-700 hover:bg-rose-50 hover:border-rose-300'
                          : 'border-emerald-200 text-emerald-700 hover:bg-emerald-50 hover:border-emerald-300'
                      }`}
                    >
                      {u.is_active ? (
                        <>
                          <UserX className="h-3.5 w-3.5" />
                          Deactivate
                        </>
                      ) : (
                        <>
                          <UserCheck className="h-3.5 w-3.5" />
                          Activate
                        </>
                      )}
                    </button>
                  </td>
                </tr>
              ))}
              {filtered.length === 0 && (
                <tr>
                  <td colSpan={5} className="py-12 text-center text-slateText-muted">
                    No users found matching "{search}".
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};
